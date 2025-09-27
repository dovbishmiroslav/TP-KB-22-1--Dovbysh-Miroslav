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

pref_num = None
operation = None
is_operate = False
operations = "+-*/"

def calculate(val):
    global pref_num, operation, is_operate

    try:
        num = float(val)
        if is_operate:
            match operation:
                case "+":
                    pref_num = add(pref_num, num)
                case "-":
                    pref_num = sub(pref_num, num)
                case "*":
                    pref_num = mul(pref_num, num)
                case "/":
                    pref_num = div(pref_num, num)
            is_operate = False
        else:
            pref_num = num
    except ValueError:
        if val in operations and pref_num is not None:
            operation = val
            is_operate = True
        else:
            print("Некоректне введення")

while True:
    if pref_num == None:
        inp = input("Введи число, або 'exit' для виходу: ")
    elif not is_operate:
        inp = input(f"ваше число: {pref_num}, оберіть операцію (+, -, *, /)")
    elif is_operate:
        match operation:
            case "+":
                inp = input (f"Додати до  {pref_num} :")
            case "-":
                inp = input (f"Відняти від {pref_num}:")
            case "*":
                inp = input (f"{pref_num} Помножити на :")
            case "/":
                inp = input ( f"{pref_num} Розділити на :")
            case _:
                print("Error")
    if inp == "exit":
        print("Калькулятор завершив роботу")
        break
    else:
        calculate(inp)