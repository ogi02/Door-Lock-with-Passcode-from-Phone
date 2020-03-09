from class_database import DB

class Guest:
    def __init__(self, id, name, surname, phone_number, passcode, entry_date, expiry_date):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.passcode = passcode
        self.entry_date = entry_date
        self.expiry_date = expiry_date

    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM guests').fetchall()
            return [Guest(*row) for row in rows]

    def find_by_id(id):
        with DB() as db:
            row = db.execute('SELECT * FROM guests WHERE id = ?', (id,)).fetchone()
            return Guest(*row)
    
    def create(self):
        with DB() as db:
            values = (self.name, self.surname, self.phone_number, self.passcode, self.entry_date, self.expiry_date,)
            db.execute('''INSERT INTO guests (name, surname, phone_number, passcode, entry_date, expiry_date) VALUES (?, ?, ?, ?, ?, ?)''', values)

    def save(self):
        with DB() as db:
            values = (self.name, self.surname, self.phone_number, self.passcode, self.entry_date, self.expiry_date, self.id)
            db.execute('''UPDATE guests SET name = ?, surname = ?, phone_number = ?, passcode = ?, entry_date = ?, expiry_date = ?, WHERE id = ?''', values)
