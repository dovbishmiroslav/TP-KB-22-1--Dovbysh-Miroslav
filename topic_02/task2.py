def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Ділення на нуль неможливе"

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
op = input("Оберіть операцію (+, -, *, /): ")

if op == "+":
    print("Результат:", add(a, b))
elif op == "-":
    print("Результат:", sub(a, b))
elif op == "*":
    print("Результат:", mul(a, b))
elif op == "/":
    print("Результат:", div(a, b))
else:
    print("Невірна операція")
