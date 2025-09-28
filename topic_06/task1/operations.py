from functions import add, sub, mul, div

pref_num = None
operation = None
is_operate = False
operations = "+-*/"

log1=""
log2=""
log3=""
log4=""

pref_logs = []

def check():
    if len(pref_logs) > 0:
        print("Попередні дії")
        for i in pref_logs:
            print(i)


def calculate(val):
    global pref_num, operation, is_operate, log4, log3, log2, log1, pref_logs

    try:
        num = float(val)
        if is_operate:

            log1 = str(pref_num)
            log2 = str(operation)
            log3 = str(num)

            match operation:
                case "+":
                    pref_num = add(pref_num, num)
                case "-":
                    pref_num = sub(pref_num, num)
                case "*":
                    pref_num = mul(pref_num, num)
                case "/":
                    pref_num = div(pref_num, num)
            
            log4 = str(pref_num)

            is_operate = False
            final_log = f"{log1} {log2} {log3}= {log4}"
            pref_logs.append(final_log)
            if len(pref_logs) > 5:
                pref_logs.pop(0)
        else:
            pref_num = num
    except ValueError:
        if val in operations and pref_num is not None:
            operation = val
            is_operate = True
        else:
            print("Некоректне введення")

def work():
    global pref_num, operation, is_operate, pref_logs

    while True:
        if pref_num is None:
            check()
            inp = input("Введи число, або 'exit' для виходу: ")
        elif not is_operate:
            check()
            inp = input(f"Ваше число: {pref_num}, оберіть операцію (+, -, *, /): ")
        elif is_operate:
            check()
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
