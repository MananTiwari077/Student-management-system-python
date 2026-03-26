class Student:
    def __init__(self, name, marks):
        self.name = name.strip()
        self.marks = marks

    def display(self):
        print(f"{self.name} - {self.marks}")