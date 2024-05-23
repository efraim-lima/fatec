import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

import bleach
import datetime
import sqlite3
import re
import uuid
import contextlib
from logs.logs import info, error, warn, critic

# Initialize logger
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

def validation(input_string):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, input_string))


@contextlib.contextmanager
def get_db_connection():
    conn = sqlite3.connect('purchases.db', check_same_thread=False)
    warn(f"database | {now} | ACTIVATED")
    try:
        yield conn
        warn(f"conn | {now} | YELD")
    finally:
        warn(f"conn | {now} | RETURN")
        return

def create_purchases():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS history (
                            id BLOB NOT NULL PRIMARY KEY,
                            ticker TEXT NOT NULL,
                            amount INTEGER NOT NULL,
                            date DATE NOT NULL,
                            operation TEXT NOT NULL
                        );""")
        warn(f"table history | {now} | CREATED")

        cursor.execute("""CREATE TABLE IF NOT EXISTS total (
                            total_id BLOB NOT NULL,
                            ticker TEXT NOT NULL,
                            amount INTEGER NOT NULL,
                            date DATE NOT NULL,
                            FOREIGN KEY (total_id) REFERENCES history(id)
                        );""")
        warn(f"table total | {now} | CREATED")

        conn.commit()

def total(ticker):
        with get_db_connection() as conn:
            warn("ENTREI POOOO")
            cursor = conn.cursor()
            cursor.execute("SELECT total_id, amount FROM total WHERE ticker=:ticker;", {'ticker': ticker})
            one = cursor.fetchone()
            
            if one:
                # history_id = cursor.lastrowid()
                total_amount = one[1]
                info(f"ticker={ticker}, total={total_amount} | {now} | TOTAL CHECKED")
                return total_amount
            else:
                info(f"\n{one}\n\n\n")
                try:
                    cursor.execute("SELECT id, amount FROM history WHERE ticker = :ticker", {'ticker': ticker})
                    existing_tickers = cursor.fetchall()
                    total_amount = sum(row[1] for row in existing_tickers)                
                    info(f"ticker={ticker}, total={total_amount} | {now} | TOTAL GOT ON TRY")
                    return total_amount
                except:
                    total_amount = 0 
                    info(f"ticker={ticker}, total={total_amount} | {now} | TOTAL FAILED ON EXCEPTION")
                    return total_amount            

def check(ticker, now):
    with get_db_connection() as conn:
        if validation(ticker):
            ticker = bleach.clean(ticker)
            
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM total 
                            WHERE ticker = ? AND date(date) = ?;""", (ticker, now))
            result = cursor.fetchone()
            info(f"ticker={ticker} | {now} | DATA VALIDATION")

            if result:
                info(f"Record | {now} | UNCESSFULL RECORD")
                return result
            else:
                warn(f"No record found | {now} | NO RECORDS FOUND")
                return None
        else:
            critic(f"ticker={ticker} | {now} | INVALID INPUT")
            return "Error"

def insert(ticker, amount, now):
    with get_db_connection() as conn:
        if validation(ticker) and validation(str(amount)) == True:
            ticker = bleach.clean(ticker)
            amount = bleach.clean(str(amount))

    
            cursor = conn.cursor()
            
            id = uuid.uuid4().hex[:10].upper()
            
            cursor.execute("""INSERT INTO history (id, ticker, amount, date, operation) VALUES (
                            :id,
                            :ticker, 
                            :amount, 
                            :date,
                            :operation
                            );""", {
                                'id': id,
                                'ticker': ticker,
                                'amount': amount,
                                'date': now,
                                'operation': "BUY"
                            })
            # ticker_id = cursor.lastrowid
            conn.commit()

            info(f"total={total}, ticker={ticker}, amount={amount} | {now} | INSERTED DATA")
            total_amount = total(ticker)
            
            print(f"\n\nTOTAL:\n{total_amount}\n\n")
            
            if total_amount:
                print(total_amount)
                try:
                    print(ticker, amount, id)
                    update(ticker, amount, id)
                except:
                    warn(f"ticker={ticker} | {now} | UPDATE FAILED")
            else:
                conn.execute("""INSERT INTO total (total_id, ticker, amount, date) VALUES (
                    :total_id,
                    :ticker,
                    :amount,
                    :date
                    );""", {
                        'total_id': id,
                        'ticker': ticker,
                        'amount': amount,
                        'date': now
                    })
                info(f"ticker={ticker}, amout={amount} | {now} | ADDED TO TOTAL")

            conn.commit()
            
            warn(f"id={id}, ticker={ticker}, amount={amount} | {now} | ADDED")            
            return
        else:
            critic(f"ticker={ticker}, amount={amount} | {now} | SANITIZATION FAILED")
            return "Error"

def read():
    with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""SELECT ticker, amount, date 
                        FROM total 
                        ORDER BY date DESC 
                        LIMIT 10;"""
                        )
            results = cursor.fetchall()

            warn(f"history readed | {now} | READED")            
            return results
        
def update(ticker, new_amount, id):
    with get_db_connection() as conn:
        if validation(ticker) and validation(str(new_amount)):
            ticker = bleach.clean(ticker)
            new_amount = int(bleach.clean(str(new_amount)))  # Convert to int
            info(f"ticker={ticker}, amount={new_amount} | {now} | UPDATE DATA SANITIZED")

            cursor = conn.cursor()       
            
            cursor.execute("SELECT total_id, amount FROM total WHERE ticker=:ticker", {'ticker': ticker})
            one = cursor.fetchone()
            
            if one:
                total_amount = one[1]    
                
                cursor.execute("""
                    UPDATE total
                    SET amount = :total_amount, date = :date
                    WHERE ticker = :ticker
                """, {
                    'total_amount': total_amount + new_amount,
                    'date': now,
                    'ticker': ticker
                })
                info(f"ticker={ticker}, new_amount={new_amount} | {now} | UPDATED")
                conn.commit()
            else:
                cursor.execute("""INSERT INTO total (total_id, ticker, amount, date) VALUES (
                    :total_id,
                    :ticker, 
                    :amount, 
                    :date
                    );""", {
                        'total_id': id,
                        'ticker': ticker,
                        'amount': new_amount,
                        'date': now})
                conn.commit()
                info(f"ticker={ticker}, total_amount={total_amount} | {now} | TOTAL ADDED")
        else:
            critic(f"ticker={ticker}, new_amount={new_amount} | {now} | SANITIZATION FAILED")
            return "Error: Sanitization failed."

def delete(ticker):
    with get_db_connection() as conn:
        if validation(ticker):
            ticker = bleach.clean(ticker)
            info(f"ticker={ticker} | {now} | UPDATE DATA SANITIZED")

            cursor = conn.cursor()       
            
            cursor.execute("SELECT total_id, amount FROM total WHERE ticker=:ticker;", {'ticker': ticker})
            one = cursor.fetchone()
            
            if one:
                cursor.execute("DELETE FROM total WHERE ticker=:ticker;", {
                    'ticker': ticker})
                conn.commit()
                warn(f"ticker={ticker} | {now} | POSITION CLOSED")
            else:
                print("Error!")
                critic(f"ticker={ticker} | {now} | TICKER NOT FOUND")

def sell(ticker, total_amount, amount, now):
    with get_db_connection() as conn:
        if validation(ticker) and validation(str(amount)):
            ticker = bleach.clean(ticker)
            amount = int(bleach.clean(str(amount)))  # Convert to int

            info(f"ticker={ticker}, amount={amount} | {now} | DATA SANITIZED")

            cursor = conn.cursor()

            total_amount = total(ticker)            
            total_amount -= amount                  
                
            # No rows updated, potentially new ticker
            cursor.execute("""
                UPDATE total
                SET amount = :total_amount, date = :date
                WHERE ticker = :ticker
            """, {
                'total_amount': total_amount,
                'date': now,
                'ticker': ticker
            })
            info(f"ticker={ticker}, new_amount={amount} | {now} | SOLD")
            
            id = uuid.uuid4().hex[:10].upper()
            
            cursor.execute("""INSERT INTO history (id, ticker, amount, date, operation) VALUES (
                :id,
                :ticker, 
                :amount, 
                :date,
                :operation
                );""", {
                    'id': id,
                    'ticker': ticker,
                    'amount': amount,
                    'date': now,
                    'operation': "SELL"
                })
            
            
            conn.commit()
        

def close():
    with get_db_connection() as conn:
        warn(f"database | {now} | CLOSED")
        # Close connection
        conn.close()