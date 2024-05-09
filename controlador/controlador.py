from model.modelo import StudentModel

class StudentController:
    def __init__(self):
        self.model = StudentModel()

    def save_new_student(self, name, age, address):
        self.model.save_new_student(name, age, address)
        # Después de guardar el nuevo estudiante, no es necesario obtener todos los estudiantes aquí
        # simplemente devolvemos un indicador de que se ha guardado correctamente
        return True

    def search_student(self, id):
        student = self.model.search_student(id)
        return student

    def get_all_students(self):
        # Llamamos al método correspondiente en la clase StudentModel
        return self.model.get_all_students()
    
    def delete_student_by_id(self, id):
        self.model.delete_student_by_id(id)

    def delete_all_students(self):
        self.model.delete_all_students()