from phonebook import add_student, find_student, delete_student


def test_add_student():
    students = []
    add_student(students, "Ivan", "123")
    assert len(students) == 1
    assert students[0]["Name"] == "Ivan"


def test_find_student():
    students = [{"Name": "Ivan", "Phone": "123"}]
    result = find_student(students, "Ivan")
    assert result["Phone"] == "123"


def test_find_student_not_found():
    students = []
    assert find_student(students, "Test") is None


def test_delete_student():
    students = [
        {"Name": "Ivan", "Phone": "123"},
        {"Name": "Petro", "Phone": "456"}
    ]
    students = delete_student(students, "Ivan")
    assert len(students) == 1
    assert students[0]["Name"] == "Petro"