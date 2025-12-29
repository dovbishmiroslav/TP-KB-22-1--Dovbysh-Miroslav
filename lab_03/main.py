from student import Student
from file_utils import FileUtils

FILENAME = "data.txt"


def main():
    student_list = FileUtils.load_from_file(FILENAME)

    while True:
        print("\n1 - Додати студента")
        print("2 - Видалити студента")
        print("3 - Змінити телефон")
        print("4 - Показати список")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            name = input("Ім'я: ")
            phone = input("Телефон: ")
            group = input("Група: ")
            student_list.add_student(Student(name, phone, group))

        elif choice == "2":
            name = input("Ім'я студента: ")
            student_list.remove_student(name)

        elif choice == "3":
            name = input("Ім'я студента: ")
            phone = input("Новий телефон: ")
            student_list.update_phone(name, phone)

        elif choice == "4":
            for s in student_list.get_all():
                print(s)

        elif choice == "0":
            FileUtils.save_to_file(FILENAME, student_list)
            print("Дані збережено. Вихід.")
            break


if __name__ == "__main__":
    main()
