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
    
    def delete_student_by_id(self, id):
        cursor = self.conn.cursor()
        query = '''DELETE FROM students WHERE id = %s'''
        cursor.execute(query, (id,))
        self.conn.commit()

        # Ajustar la secuencia
        query_adjust_sequence = '''SELECT setval('students_id_seq', (SELECT COALESCE(MAX(id),0)+1 FROM students), false)'''
        cursor.execute(query_adjust_sequence)
        self.conn.commit()

    def delete_all_students(self):
        cursor = self.conn.cursor()
        query = '''DELETE FROM students'''
        cursor.execute(query)
        self.conn.commit()

        # Reiniciar la secuencia
        query_reset_sequence = '''ALTER SEQUENCE students_id_seq RESTART WITH 1'''
        cursor.execute(query_reset_sequence)
        self.conn.commit()

    def close_connection(self):
        self.conn.close()