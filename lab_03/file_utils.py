from student import Student
from student_list import StudentList


class FileUtils:
    @staticmethod
    def load_from_file(filename: str) -> StudentList:
        student_list = StudentList()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    name, phone, group = line.strip().split(";")
                    student_list.add_student(Student(name, phone, group))
        except FileNotFoundError:
            pass
        return student_list

    @staticmethod
    def save_to_file(filename: str, student_list: StudentList):
        with open(filename, "w", encoding="utf-8") as file:
            for student in student_list.get_all():
                file.write(str(student) + "\n")