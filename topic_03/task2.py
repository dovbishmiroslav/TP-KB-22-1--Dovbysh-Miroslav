def test_list_functions():
    lst = [1, 2, 3]
    print("Початковий список:", lst)

    lst.append(4)
    print("append(4):", lst)

    lst.extend([5, 6])
    print("extend([5, 6]):", lst)

    lst.insert(2, 99)
    print("insert(2, 99):", lst)

    lst.remove(99)
    print("remove(99):", lst)

    lst_copy = lst.copy()
    print("copy():", lst_copy)

    lst.reverse()
    print("reverse():", lst)

    lst.sort()
    print("sort():", lst)

    lst.clear()
    print("clear():", lst)

test_list_functions()
