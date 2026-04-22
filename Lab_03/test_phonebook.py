from phonebook import add_student, find_student, delete_student, Student


def test_add_student():
    students = []
    add_student(students, "Ivan", "123")
    assert len(students) == 1
    assert students[0].name == "Ivan"
    assert students[0].phone == "123"


def test_find_student():
    students = [Student("Ivan", "123")]
    result = find_student(students, "Ivan")
    assert result is not None
    assert result.phone == "123"


def test_find_student_not_found():
    students = []
    assert find_student(students, "Test") is None


def test_delete_student():
    students = [
        Student("Ivan", "123"),
        Student("Petro", "456")
    ]
    students = delete_student(students, "Ivan")
    assert len(students) == 1
    assert students[0].name == "Petro"