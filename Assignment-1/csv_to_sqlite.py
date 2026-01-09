# Assignment-1/csv_to_sqlite.py
import csv
import sqlite3

conn = sqlite3.connect("users.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users(name TEXT, email TEXT)")

# CSV read aur insert
with open("data/users.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        cur.execute("INSERT INTO users VALUES (?,?)", (row["name"], row["email"]))

conn.commit()

# Database read aur print
for row in cur.execute("SELECT * FROM users"):
    print(row)

conn.close()
