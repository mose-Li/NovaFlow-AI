import sqlite3

conn = sqlite3.connect("database/novaflow.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(documents)")

for row in cursor.fetchall():
    print(row)

conn.close()