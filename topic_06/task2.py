st = [
    {"Mark": 80, "Name": "Jon"},
    {"Mark": 50, "Name": "Zak"},
    {"Mark": 60, "Name": "Bob"}
]
sort_by_Mark = sorted(st, key=lambda x: x["Mark"])
sort_by_Name = sorted(st, key=lambda x: x["Name"])
print(sort_by_Mark)
print(sort_by_Name)