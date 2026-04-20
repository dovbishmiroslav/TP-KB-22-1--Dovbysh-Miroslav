import csv
import sys


def load_students(filename):
    students = []
    try:
        with open(filename, newline='', encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                students.append({
                    "Name": row["Name"],
                    "Phone": row["Phone"]
                })
    except FileNotFoundError:
        print("Файл не знайдено!")
    return students


def save_students(filename, students):
    with open(filename, "w", newline='', encoding="utf-8") as file:
        fieldnames = ["Name", "Phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            writer.writerow(student)


def add_student(students, name, phone):
    students.append({"Name": name, "Phone": phone})


def find_student(students, name):
    for student in students:
        if student["Name"].lower() == name.lower():
            return student
    return None


def delete_student(students, name):
    return [s for s in students if s["Name"].lower() != name.lower()]


def show_students(students):
    for student in students:
        print(f"{student['Name']} - {student['Phone']}")


def main():
    if len(sys.argv) < 2:
        print("Вкажіть CSV файл!")
        return

    filename = sys.argv[1]
    students = load_students(filename)

    while True:
        print("\n1. Показати всіх")
        print("2. Додати")
        print("3. Знайти")
        print("4. Видалити")
        print("5. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            show_students(students)

        elif choice == "2":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            add_student(students, name, phone)

        elif choice == "3":
            name = input("Ім'я: ")
            student = find_student(students, name)
            print(student if student else "Не знайдено")

        elif choice == "4":
            name = input("Ім'я: ")
            students = delete_student(students, name)

        elif choice == "5":
            save_students("students_out.csv", students)
            print("Збережено!")
            break

        else:
            print("Невірний вибір!")


if __name__ == "__main__":
    main()