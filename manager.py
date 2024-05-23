import sqlite3

class Manager:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('sucursalvirtual.db', check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            lastname TEXT,
            rut TEXT,
            email TEXT,
            phone TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_student(self, name, lastname, rut, email, phone):
        query = "INSERT INTO students (name, lastname, rut, email, phone) VALUES (?, ?, ?, ?, ?)"
        self.conn.execute(query, (name, lastname, rut, email, phone))
        self.conn.commit()

    def get_student(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM students"
        cursor.execute(query)
        students = cursor.fetchall()
        return students
    
    def delete_student(self, rut):
        query = "DELETE FROM students WHERE rut = ?"
        self.conn.execute(query, (rut,))
        self.conn.commit()

    def update_student(self, name, lastname, rut, email, phone):
        query = "UPDATE students SET name = ?, lastname = ?, email = ?, phone = ? WHERE rut = ?"
        self.conn.execute(query, (name, lastname, email, phone, rut))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

