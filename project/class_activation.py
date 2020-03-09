from class_database import DB

class Activation:
	def __init__(self, id, key, active):
		self.id = id
		self.key = key
		self.active = active

	def get_by_key(key):
		with DB() as db:
			row = db.execute('SELECT * FROM activation WHERE key = ?', (key, )).fetchone()
			return Activation(*row)

	def activate(key):
		with DB() as db:
			row = db.execute('UPDATE activation SET active = 1 WHERE key = ?', (key, )).fetchone()
