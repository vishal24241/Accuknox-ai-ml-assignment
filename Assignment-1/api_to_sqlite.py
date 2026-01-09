# Assignment-1/api_to_sqlite.py
import requests
import sqlite3

# Step 1: API se data fetch karna
response = requests.get("https://jsonplaceholder.typicode.com/posts")
books_data = response.json()[:5]  # sirf pehle 5 records

# Step 2: Database connection aur table create
conn = sqlite3.connect("books.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER,
title TEXT,
author TEXT,
year INTEGER
)
""")

# Step 3: Data insert karna
for book in books_data:
    cur.execute("INSERT INTO books VALUES (?,?,?,?)", (book["id"], book["title"], "Unknown", 2024))

conn.commit()

# Step 4: Data read aur print
for row in cur.execute("SELECT * FROM books"):
    print(row)

conn.close()


