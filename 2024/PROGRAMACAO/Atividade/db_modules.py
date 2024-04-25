import sqlite3
 
def create_table_if_not_exists(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        address TEXT NOT NULL
                    )''')
    conn.commit()
 
def check_for_conflict(conn, name):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users WHERE name=?", (name,))
    result = cursor.fetchone()
    return result is not None
 
def insert_user(conn, name, address):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, address) VALUES (?, ?)", (name, address))
    conn.commit()
    print("User added successfully.")
 
def main():
    # Connect to SQLite database
    conn = sqlite3.connect('example.db')
 
    # Create table if it doesn't exist
    create_table_if_not_exists(conn)
 
    # Receive user input
    name = input("Enter name: ")
    address = input("Enter address: ")
 
    # Check for conflicts
    if check_for_conflict(conn, name):
        print("Error: A user with this name already exists.")
    else:
        # Insert user if no conflict
        insert_user(conn, name, address)
 
    # Close connection
    conn.close()
 
if __name__ == "__main__":
    main()
