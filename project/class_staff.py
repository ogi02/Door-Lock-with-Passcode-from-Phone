from class_database import DB

class Staff:
    def __init__(self, id, name, surname, phone_number, position, passcode):
        self.id = id
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.position = position
        self.passcode = passcode

    def all():
        with DB() as db:
            rows = db.execute('SELECT * FROM staff').fetchall()
            return [Staff(*row) for row in rows]

    def find_by_id(id):
        with DB() as db:
            row = db.execute('SELECT * FROM staff WHERE id = ?', (id,)).fetchone()
            return Staff(*row)
    
    def create(self):
        with DB() as db:
            values = (self.name, self.surname, self.phone_number, self.position, self.passcode)
            db.execute('''INSERT INTO staff (name, surname, phone_number, position, passcode) VALUES (?, ?, ?, ?, ?)''', values)

    def save(self):
        with DB() as db:
            values = (self.name, self.surname, self.phone_number, self.position, self.passcode, self.id)
            db.execute('''UPDATE staff SET name = ?, surname = ?, phone_number = ?, position = ?, passcode = ? WHERE id = ?''', values)
