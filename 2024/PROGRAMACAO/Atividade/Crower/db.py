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
    warn(f"database conn activated at {now}")
    try:
        yield conn
        warn(f"conn yeld at {now}")
    finally:
        warn(f"return of conn at {now}")
        return

def create_purchases():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS history (
                            id BLOB NOT NULL PRIMARY KEY,
                            ticker TEXT NOT NULL,
                            amount INTEGER NOT NULL,
                            date DATE NOT NULL
                        );""")
        warn(f"table history created at {now}")

        cursor.execute("""CREATE TABLE IF NOT EXISTS total (
                            total_id BLOB NOT NULL,
                            ticker TEXT NOT NULL,
                            amount INTEGER NOT NULL,
                            date DATE NOT NULL,
                            FOREIGN KEY (total_id) REFERENCES history(id)
                        );""")
        warn(f"table total created at {now}")

        conn.commit()

def check(ticker, now):
    with get_db_connection() as conn:
        if validation(ticker):
            ticker = bleach.clean(ticker)
            
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM history 
                            WHERE ticker = ? AND date(date) = ?;""", (ticker, now))
            result = cursor.fetchone()
            info(f"data validation: {ticker} at {now}")

            if result:
                info(f"Record found successfully at {now}")
                return result
            else:
                warn(f"No record found for the given criteria. at {now}")
                return None
        else:
            critic(f"Invalid input for ticker={ticker} at {now}.")
            return "Error"

def insert(ticker, amount, now):
    with get_db_connection() as conn:
        if validation(ticker) and validation(str(amount)) == True:
            ticker = bleach.clean(ticker)
            amount = bleach.clean(str(amount))

            info(f"data sanitized: ticker={ticker}, amount={amount} and date={now} at {now}")
    
            cursor = conn.cursor()
            
            id = uuid.uuid4().hex[:10].upper()
            print(f"\n\n\n\n{id}\n\n\n\n")
            
            cursor.execute("""INSERT INTO history (id, ticker, amount, date) VALUES (
                            :id,
                            :ticker, 
                            :amount, 
                            :date
                            );""", {
                                'id': id,
                                'ticker': ticker,
                                'amount': amount,
                                'date': now
                            })

            ticker_id = cursor.lastrowid
            conn.commit()
            
            try:
                update(ticker, amount, now, id)
            except:
                print("ERRRRROOOOOOOOOOOU")
                
            warn(f"id={id}, ticker={ticker}, amount={amount} | {now} | ADDED")            
            return
        else:
            critical(f"ticker={ticker}, amount={amount} | {now} | SANITIZATION FAILED")
            return "Error"

def read():
    with get_db_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute("""SELECT * 
                        FROM history 
                        ORDER BY date DESC 
                        LIMIT 10;"""
                        )
            results = cursor.fetchall()
            print(results)
            
            if results == None:
                results = "Não há operações salvas!\n"

            warn(f"id={id}, ticker={ticker}, amount={amount} | {now} | ADDED")            
            return results
        
def update(ticker, new_amount, now, id):
    with get_db_connection() as conn:
        print(f"\n\n\n\n UPDATE!\n1{id} \n\n\n\n")
        if validation(ticker) and validation(str(new_amount)):
            ticker = bleach.clean(ticker)
            new_amount = int(bleach.clean(str(new_amount)))  # Convert to int

            info(f"ticker={ticker}, amount={new_amount} | {now} | SANITIZED")

            cursor = conn.cursor()
            print(f"\n\n\n\n UPDATE!\n1\n{id} \n\n\n\n")

            cursor.execute("SELECT id, amount FROM history WHERE ticker = :ticker", {'ticker': ticker})
            print(f"\n\n\n\n UPDATE!\n2\n{id} \n\n\n\n")
            # history_id = cursor.lastrowid()
            existing_tickers = cursor.fetchall()
            print(f"\n\n\n\n UPDATE!\n3\n{existing_tickers} \n\n\n\n")

            if existing_tickers:
                total_amount = sum(row[1] for row in existing_tickers) + new_amount
                print(f"\n\n\n\n UPDATE!\n4\n{len(existing_tickers)} \n\n\n\n")
                print(f"\n\n\n\n UPDATE!\n5\n{total_amount} \n\n\n\n")
                try:
                    
                    print(f"\n\n\n\n UPDATE!\n5\n{total_amount} \n\n\n\n")
                    # No rows updated, potentially new ticker
                    if cursor.lastrowid == 0:
                        cursor.execute("""INSERT INTO total (total_id, ticker, amount, date) VALUES (
                            :total_id,
                            :ticker, 
                            :amount, 
                            :date
                            );""", {
                                'total_id': id,
                                'ticker': ticker,
                                'amount': total_amount,
                                'date': now})
                        info(f"ticker={ticker}, total_amount={total_amount} | {now} | TOTAL ADDED")
                    
                    cursor.execute("""
                        UPDATE total
                        SET amount = :total_amount, date = :date
                        WHERE ticker = :ticker
                    """, {
                        'total_amount': total_amount,
                        'date': now,
                        'ticker': ticker
                    })
                    info(f"ticker={ticker}, new_amount={new_amount} | {now} | UPDATED")
                    conn.commit()

                except sqlite3.Error as e:
                    print(e)
                    error(f"Error updating total table: {e}")
                    return "Error: Database error occurred."
                return
            else:
                warn(f"No data found for ticker={ticker}.")
                return "Error: No data found."
        else:
            critical(f"ticker={ticker}, new_amount={new_amount} | {now} | SANITIZATION FAILED")
            return "Error: Sanitization failed."


def delete(ticker, amount, now):
    with get_db_connection() as conn:
        print(f"\n\n\n\n UPDATE!\n1{id} \n\n\n\n")
        if validation(ticker) and validation(str(new_amount)):
            ticker = bleach.clean(ticker)
            new_amount = int(bleach.clean(str(new_amount)))  # Convert to int

            info(f"ticker={ticker}, amount={new_amount} | {now} | SANITIZED")

            cursor = conn.cursor()
            print(f"\n\n\n\n UPDATE!\n1\n{id} \n\n\n\n")

            cursor.execute("SELECT id, amount FROM history WHERE ticker = :ticker", {'ticker': ticker})
            print(f"\n\n\n\n UPDATE!\n2\n{id} \n\n\n\n")
            # history_id = cursor.lastrowid()
            existing_tickers = cursor.fetchall()
            print(f"\n\n\n\n UPDATE!\n3\n{existing_tickers} \n\n\n\n")

            if existing_tickers:
                total_amount = sum(row[1] for row in existing_tickers)
                print(f"\n\n\n\n UPDATE!\n4\n{len(existing_tickers)} \n\n\n\n")
                print(f"\n\n\n\n UPDATE!\n5\n{total_amount} \n\n\n\n")

                if amount <= total_amount:
                    total_amount -= amount
                    try:             
                        print(f"\n\n\n\n UPDATE!\n5\n{total_amount} \n\n\n\n")
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
                        info(f"ticker={ticker}, new_amount={new_amount} | {now} | DELETED")
                        conn.commit()

                    except sqlite3.Error as e:
                        print(e)
                        error(f"Error updating total table: {e}")
                        return "Error: Database error occurred."
                    return
                else:
                    warn(f"No data found for ticker={ticker}.")
                    return "Error: No data found."
            else:
                critical(f"ticker={ticker}, new_amount={new_amount} | {now} | SANITIZATION FAILED")
                return "Error: Sanitization failed."

def get_amount_sum(stock_symbol):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM history WHERE ticker=?;", (stock_symbol,))
        result = cursor.fetchone()

        if result:
            info(f"ticker={stock_symbol} | {now} | SUM GOT")            
            return result[0] if result else 0
        else:
            warn(f"ticker={stock_symbol} | {now} | NOT FETCHED")
            return 0

def close():
    with get_db_connection() as conn:
        warn(f"database closed at {now}")
        # Close connection
        conn.close()