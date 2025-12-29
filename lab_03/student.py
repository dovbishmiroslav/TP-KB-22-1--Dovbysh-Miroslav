class Student:
    def __init__(self, name: str, phone: str, group: str):
        self.name = name
        self.phone = phone
        self.group = group

    def __str__(self):
        return f"{self.name};{self.phone};{self.group}"

    def update_phone(self, new_phone: str):
        self.phone = new_phone