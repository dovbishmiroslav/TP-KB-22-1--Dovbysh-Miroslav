def find_insert_position(sorted_list, new_element):
    for i, val in enumerate(sorted_list):
        if new_element < val:
            return i
    return len(sorted_list)

lst = [1, 3, 5, 7, 9]
num = int(input("Введи число для вставки"))
pos = find_insert_position(lst, num)
print(f"Позиція для вставки {num} у {lst}: {pos}")
