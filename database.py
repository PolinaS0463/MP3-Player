import sqlite3 as sq

DATABASE_PATH = "songs_database.db"

def create_table() -> None:
    with sq.connect(DATABASE_PATH) as con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS songs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        path TEXT,
                        singer TEXT,
                        rating INTEGER
                    )""")
    