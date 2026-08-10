import sqlite3

conn = sqlite3.connect("database/novaflow.db")

cursor = conn.execute(
    "PRAGMA table_info(embeddings)"
)

for row in cursor:
    print(row)

conn.close()