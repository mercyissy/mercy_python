import sqlite3

def get_transactions():
    # Connect to the SQLite database
    conn = sqlite3.connect('bank_transactions.db')
    cursor = conn.cursor()

    # Query to retrieve transaction details
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    # Close the connection
    conn.close()

    return transactions

def display_transactions(transactions):
    print("Transaction History:")
    print(f"{'ID':<5} {'Date':<15} {'Description':<20} {'Amount':<10}")
    print("-" * 60)
    for transaction in transactions:
        print(f"{transaction[0]:<5} {transaction[1]:<15} {transaction[2]:<20} {transaction[3]:<10.2f}")

if __name__ == "__main__":
    transactions = get_transactions()
    display_transactions(transactions)


import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('bank_transactions.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table for transactions
cursor.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL
)
''')

# Insert some sample data
cursor.execute("INSERT INTO transactions (date, description, amount) VALUES ('2023-01-01', 'Deposit', 1000.00)")
cursor.execute("INSERT INTO transactions (date, description, amount) VALUES ('2023-01-05', 'Withdrawal', -200.00)")
cursor.execute("INSERT INTO transactions (date, description, amount) VALUES ('2023-01-10', 'Transfer', -150.00)")
cursor.execute("INSERT INTO transactions (date, description, amount) VALUES ('2023-01-15', 'Payment', -50.00)")

# Commit the changes and close the connection
conn.commit()
conn.close()