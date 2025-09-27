def test_dict_functions():
    d = {"a": 1, "b": 2}
    print("Початковий словник:", d)

    d.update({"c": 3})
    print("update({'c': 3}):", d)

    print("keys():", list(d.keys()))

    print("values():", list(d.values()))

    print("items():", list(d.items()))

    del d["b"]
    print("del d['b']:", d)

    d.clear()
    print("clear():", d)

test_dict_functions()