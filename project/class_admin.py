import hashlib
from class_database import DB

class Admin:
	def __init__(self, id, username, name, surname, password, passcode):
		self.id = id
		self.username = username
		self.name = name
		self.surname = surname
		self.password = password
		self.passcode = passcode

	@staticmethod
	def all():
		with DB() as db:
			rows = db.execute('SELECT * FROM admins').fetchall()
			return [Admin(*row) for row in rows]

	@staticmethod
	def all_usernames():
		with DB() as db:
			rows = db.execute('SELECT * FROM admins').fetchall()
			return [Admin(*row).username for row in rows]

	@staticmethod
	def find_by_username(username):
		if not username:
			return None
		with DB() as db:
			row = db.execute('SELECT * FROM admins WHERE username = ?', (username,)).fetchone()
			if row:
				return Admin(*row)

	def create(self):
		with DB() as db:
			values = (self.username, self.name, self.surname, self.password, self.passcode)
			db.execute('INSERT INTO admins (username, name, surname, password, passcode) VALUES (?, ?, ?, ?, ?)', values)

	def save(self):
		with DB() as db:
			values = (self.username, self.name, self.surname, self.password, self.passcode, self.id)
			db.execute('UPDATE admins SET username = ?, name = ?, surname = ?, password = ?, passcode = ? WHERE id = ?', values)
			return self

	@staticmethod
	def hash_password(password):
		return hashlib.sha256(password.encode('utf-8')).hexdigest()

	def verify_password(self, password):
		return self.password == hashlib.sha256(password.encode('utf-8')).hexdigest()