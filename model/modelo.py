import psycopg2

class StudentModel:
    def save_new_student(self, name, age, address):
        conn = psycopg2.connect(dbname="postgres", user="postgres",
                                password="ads123", host="localhost", port="5432")
        cursor = conn.cursor()
        query = '''INSERT INTO students(name, age, address) VALUES (%s, %s, %s)'''
        cursor.execute(query, (name, age, address))
        conn.commit()
        conn.close()

    def search_student(self, id):
        conn = psycopg2.connect(dbname="postgres", user="postgres",
                                password="ads123", host="localhost", port="5432")
        cursor = conn.cursor()
        query = '''SELECT * FROM students where id=%s'''
        cursor.execute(query, (id))
        row = cursor.fetchone()
        conn.close()
        return row
