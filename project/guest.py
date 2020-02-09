from database import DB

class Guest:
    def __init__(self, id, name, surname, passcode, phone_number, entry_date, expiry_date, has_entered):
        self.id = id
        self.name = name
        self.surname = surname
        self.passcode = passcode
        self.phone_number = phone_number
        self.entry_date = entry_date
        self.expiry_date = expiry_date
        self.has_entered = has_entered

    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM guests').fetchall()
            return [Guest(*row) for row in rows]

    def find(id):
        with DB() as db:
            row = db.execute('SELECT * FROM guests WHERE id = ?', (id,)).fetchone()
            return Guest(*row)
    
    def create(self):
        with DB() as db:
            values = (
                self.name,
                self.surname,
                self.passcode,
                self.phone_number,
                self.entry_date,
                self.expiry_date,
                self.has_entered
            )
            row = db.execute('INSERT INTO guests (name, surname, passcode, phone_number, entry_date, expiry_date, has_entered) VALUES (?, ?, ?, ?, ?, ?, ?)', values)
            return self

    def save(self):
        with DB() as db:
            values = (
                self.name,
                self.surname,
                self.passcode,
                self.phone_number,
                self.entry_date,
                self.expiry_date,
                self.has_entered,
                self.id
            )
            row = db.execute('UPDATE guests SET name = ?, surname = ?, passcode = ?, phone_number = ?, entry_date = ?, expiry_date = ?, has_entered = ? WHERE id = ?', values)
            return self

    def delete(self):
        with DB() as db:
            db.execute('DELETE FROM guests WHERE id = ?', (self.id,))
