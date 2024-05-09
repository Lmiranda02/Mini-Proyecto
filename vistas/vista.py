from tkinter import Tk, Canvas, Frame, Label, Entry, Button, Listbox, END
from controlador.controlador import StudentController

class StudentView:
    def __init__(self, root):
        self.root = root
        self.root.title("Python & PosgreSQL")

        self.canvas = Canvas(self.root, height=380, width=400)
        self.canvas.pack()

        self.frame = Frame()
        self.frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.label = Label(self.frame, text="Add a Student")
        self.label.grid(row=0, column=1)

        # Name Input
        self.label_name = Label(self.frame, text="Name")
        self.label_name.grid(row=1, column=0)

        self.entry_name = Entry(self.frame)
        self.entry_name.grid(row=1, column=1)
        self.entry_name.focus()

        # Age
        self.label_age = Label(self.frame, text="Age")
        self.label_age.grid(row=2, column=0)

        self.entry_age = Entry(self.frame)
        self.entry_age.grid(row=2, column=1)

        # Address
        self.label_address = Label(self.frame, text="Address")
        self.label_address.grid(row=3, column=0)

        self.entry_address = Entry(self.frame)
        self.entry_address.grid(row=3, column=1)

        # Button
        self.button_add = Button(self.frame, text="Add", command=self.add_student)
        self.button_add.grid(row=4, column=1)

        # Search
        self.label_search = Label(self.frame, text="Search Data")
        self.label_search.grid(row=5, column=1)

        self.label_id = Label(self.frame, text="Search By ID")
        self.label_id.grid(row=6, column=0)

        self.entry_id = Entry(self.frame)
        self.entry_id.grid(row=6, column=1)

        self.button_search = Button(self.frame, text="Search", command=self.search_student)
        self.button_search.grid(row=6, column=2)
        
        # Botón Eliminar por ID
        self.button_delete_by_id = Button(self.frame, text="Delete by ID", command=self.delete_student_by_id)
        self.button_delete_by_id.grid(row=7, column=1)

        # Botón Eliminar todos los estudiantes
        self.button_delete_all = Button(self.frame, text="Delete All", command=self.delete_all_students)
        self.button_delete_all.grid(row=8, column=1)

        self.listbox = Listbox(self.frame, width=20, height=5)
        self.listbox.grid(row=10, columnspan=4)

    def add_student(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        address = self.entry_address.get()
        self.controller = StudentController()
        self.controller.save_new_student(name, age, address)
        self.list_students()

    def search_student(self):
        id = self.entry_id.get()
        self.controller = StudentController()
        student = self.controller.search_student(id)
        self.listbox.delete(0, END)  # Limpiar la lista antes de mostrar el estudiante encontrado
        if student:
            self.listbox.insert(END, student)

    def list_students(self):
        # Limpiar la lista antes de mostrar los estudiantes
        self.listbox.delete(0, END)
        # Obtener todos los estudiantes y mostrarlos en el listbox
        self.controller = StudentController()
        students = self.controller.get_all_students()
        for student in students:
            self.listbox.insert(END, student)

    def delete_student_by_id(self):
        id = self.entry_id.get()
        self.controller = StudentController()
        self.controller.delete_student_by_id(id)
        # Actualizar la lista después de eliminar el estudiante
        self.list_students()

    def delete_all_students(self):
        self.controller = StudentController()
        self.controller.delete_all_students()
        # Limpiar la lista después de eliminar todos los estudiantes
        self.listbox.delete(0, END)
