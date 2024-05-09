from model.modelo import StudentModel

class StudentController:
    def save_new_student(self, name, age, address):
        model = StudentModel()
        model.save_new_student(name, age, address)

    def search_student(self, id):
        model = StudentModel()
        student = model.search_student(id)
        return student
