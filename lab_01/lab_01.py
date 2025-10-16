students = [
    {"name": "Bob", "phone": "0631111111", "email": "bob@gmail.com", "address": "Kyiv"},
    {"name": "Emma", "phone": "0632222222", "email": "emma@gmail.com", "address": "Lviv"},
    {"name": "Jon", "phone": "0633333333", "email": "jon@gmail.com", "address": "Odessa"},
    {"name": "Zak", "phone": "0634444444", "email": "zak@gmail.com", "address": "Dnipro"}
]

def printAllList():
    for e in students:
        strForPrint = (
            f"Name: {e['name']}, "
            f"Phone: {e['phone']}, "
            f"Email: {e['email']}, "
            f"Address: {e['address']}"
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")

    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        del students[deletePosition]
        print("Element has been deleted")
    return

def updateElement():
    name = input("Please enter name of the student to update: ")
    found = None
    for item in students:
        if item["name"] == name:
            found = item
            break
    if not found:
        print("Student not found")
        return

    new_name = input(f"New name (current: {found['name']}): ") or found['name']
    new_phone = input(f"New phone (current: {found['phone']}): ") or found['phone']
    new_email = input(f"New email (current: {found['email']}): ") or found['email']
    new_address = input(f"New address (current: {found['address']}): ") or found['address']

    students.remove(found)

    newItem = {"name": new_name, "phone": new_phone, "email": new_email, "address": new_address}

    insertPosition = 0
    for item in students:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)

    print("Student has been updated")
    return

def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List of students:")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong choice")

main()
