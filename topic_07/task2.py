

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Студент: {self.name}, вік: {self.age}"
    
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age})"

st1 = Student("Оля", 20)
print(st1.age)
print(st1.name)
print(st1)
print([st1])