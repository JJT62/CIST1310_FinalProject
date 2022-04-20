import sqlite3 as sql

conn = sql.connect("database.db")

conn.execute("CREATE TABLE products (name TEXT, description TEXT, quantity TEXT, checkin TEXT)")

conn.close()

print("Table created successfully")