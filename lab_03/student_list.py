from student import Student


class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, name: str):
        self.students = [s for s in self.students if s.name != name]

    def find_student(self, name: str):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def update_phone(self, name: str, new_phone: str):
        student = self.find_student(name)
        if student:
            student.update_phone(new_phone)

    def get_all(self):
        return self.students