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

match op:
    case "+":
        print("Результат:", add(a, b))
    case "-":
        print("Результат:", sub(a, b))
    case "*":
        print("Результат:", mul(a, b))
    case  "/":
        print("Результат:", div(a, b))
    case _:
        print("Невірна операція")