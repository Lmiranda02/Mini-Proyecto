from tkinter import Tk
from vistas.vista import StudentView

def main():
    root = Tk()
    student_view = StudentView(root)
    root.mainloop()

if __name__ == "__main__":
    main()
