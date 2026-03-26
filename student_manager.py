from students import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks):
        self.students.append(Student(name, marks))
        print("Student added!")

    def view_students(self):
        if not self.students:
            print("No students found")
        else:
            for s in self.students:
                s.display()

    def search_student(self, name):
        for s in self.students:
            if s.name.lower() == name.strip().lower():
                print("Found:", s.name, "-", s.marks)
                return
        print("Student not found")

    def delete_student(self, name):
        for s in self.students:
            if s.name.lower() == name.strip().lower():
                self.students.remove(s)
                print("Student deleted")
                return
        print("Student not found")

    def update_student(self, name, new_marks):
        for s in self.students:
            if s.name.lower() == name.strip().lower():
                s.marks = new_marks
                print("Marks updated")
                return
        print("Student not found")

    def save_to_file(self):
        with open("students.txt", "w") as f:
            for s in self.students:
                f.write(f"{s.name},{s.marks}\n")

    def load_from_file(self):
        try:
            with open("students.txt", "r") as f:
                for line in f:
                    name, marks = line.strip().split(",")
                    self.students.append(Student(name, int(marks)))
        except FileNotFoundError:
            pass