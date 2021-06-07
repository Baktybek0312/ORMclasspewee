import sqlite3


with sqlite3.connect("database.db") as db:
    cursor = db.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id
    INTEGER, name TEXT)""")
    db.commit()
