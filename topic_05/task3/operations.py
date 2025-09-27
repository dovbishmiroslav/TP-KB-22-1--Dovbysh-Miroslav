from functions import add, sub, mul, div

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

def work():
    global pref_num, operation, is_operate

    while True:
        if pref_num is None:
            inp = input("Введи число, або 'exit' для виходу: ")
        elif not is_operate:
            inp = input(f"Ваше число: {pref_num}, оберіть операцію (+, -, *, /): ")
        elif is_operate:
            match operation:
                case "+":
                    inp = input(f"Додати до {pref_num}: ")
                case "-":
                    inp = input(f"Відняти від {pref_num}: ")
                case "*":
                    inp = input(f"{pref_num} помножити на: ")
                case "/":
                    inp = input(f"{pref_num} розділити на: ")
                case _:
                    print("Помилка")
        if inp == "exit":
            print("Калькулятор завершив роботу")
            break
        else:
            calculate(inp)
