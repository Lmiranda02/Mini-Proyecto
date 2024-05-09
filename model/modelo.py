import psycopg2

class StudentModel:
    def __init__(self):
        self.conn = psycopg2.connect(dbname="postgres", user="postgres",
                                      password="ads123", host="localhost", port="5432")

    def save_new_student(self, name, age, address):
        cursor = self.conn.cursor()
        query = '''INSERT INTO students(name, age, address) VALUES (%s, %s, %s)'''
        cursor.execute(query, (name, age, address))
        self.conn.commit()

    def search_student(self, id):
        cursor = self.conn.cursor()
        query = '''SELECT * FROM students where id=%s'''
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        return row

    def get_all_students(self):
        cursor = self.conn.cursor()
        query = '''SELECT * FROM students'''
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def close_connection(self):
        self.conn.close()