import sqlite3 as sql
connection = sql.connect("audio.sqlite", check_same_thread=False)


def create_table():
    connection.execute("CREATE TABLE IF NOT EXISTS playlist"
                       "(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR, song BLOB)")
