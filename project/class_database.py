import sqlite3

DB_NAME = 'example.db'

conn = sqlite3.connect(DB_NAME)

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS admins
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		username TEXT,
		name TEXT,
		surname TEXT,
		password TEXT,
		passcode INTEGER
	)
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS staff 
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		surname TEXT,
		phone_number TEXT,
		position TEXT,
		passcode TEXT
	)
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS guests
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT,
		surname TEXT,
		phone_number TEXT,
		passcode TEXT,
		entry_date TEXT,
		expiry_date TEXT
	)
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS passcodes
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		passcode TEXT,
		entry_date TEXT,
		expiry_date TEXT
	)
''')

conn.cursor().execute('''
CREATE TABLE IF NOT EXISTS activation
	(
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		key TEXT,
		active INTEGER
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
