class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

students = [
    Student("Ivan", 20),
    Student("Petro", 18),
    Student("Olena", 22),
    Student("Marta", 19)
]

for s in sorted(students, key=lambda x: x.age):
    print(s.name, s.age)
