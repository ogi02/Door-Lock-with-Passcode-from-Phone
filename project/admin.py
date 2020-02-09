from database import DB

class Admin:
    def __init__(self, id, name, surname, password, passcode):
        self.id = id
        self.name = name
        self.surname = surname
        self.password = password
        self.passcode = passcode

    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM admins').fetchall()
            return [Admin(*row) for row in rows]

    def find(id):
        with DB() as db:
            row = db.execute('SELECT * FROM admins WHERE id = ?', (id,)).fetchone()
            return Admin(*row)
    
    def create(self):
        with DB() as db:
            values = (
                self.name,
                self.surname,
                self.password,
                self.passcode,
            )
            row = db.execute('INSERT INTO admins (name, surname, password, passcode) VALUES (?, ?, ?, ?)', values)
            return self

    def save(self):
        with DB() as db:
            values = (
                self.name,
                self.surname,
                self.password,
                self.passcode,
                self.id
            )
            row = db.execute('UPDATE admins SET name = ?, surname = ?, password = ?, passcode = ?  WHERE id = ?', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM admins WHERE id = ?', (self.id,))
