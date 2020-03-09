from class_database import DB

class Passcode:
	def __init__(self, id, passcode, entry_date, expiry_date):
		self.id = id
		self.passcode = passcode
		self.entry_date = entry_date
		self.expiry_date = expiry_date

	def create(self):
		with DB() as db:
			values = (self.passcode, self.entry_date, self.expiry_date)
			row = db.execute('INSERT INTO passcodes (passcode, entry_date, expiry_date) VALUES (?, ?, ?)', values)

	@staticmethod
	def all():
		with DB() as db:
			rows = db.execute('SELECT * FROM passcodes').fetchall()
			return [Passcode(*row).passcode for row in rows]

	def get_by_passcode(passcode):
		with DB() as db:
			row = db.execute('SELECT * FROM passcodes WHERE passcode = ?', (passcode, )).fetchone()
			if row:
				return Passcode(*row)
