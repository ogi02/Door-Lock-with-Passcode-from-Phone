import sqlite3

DB_NAME = 'example.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS admins
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        password TEXT NOT NULL,
        passcode INTEGER NOT NULL
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS staff 
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        passcode INTEGER NOT NULL,
        type TEXT NOT NULL
    )
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS guests
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        passcode INTEGER NOT NULL,
        phone_number INTEGER NOT NULL,
        entry_date TEXT NOT NULL,
        expiry_date TEXT NOT NULL,
        has_entered INTEGER NOT NULL
    )
''')

conn.commit()


class DB:
    def __enter__(self):
        self.conn = sqlite3.connect(DB_NAME)
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
        self.conn.commit()

conn.close()
