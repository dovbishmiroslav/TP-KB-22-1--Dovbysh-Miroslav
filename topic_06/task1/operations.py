
def show_previous_logs(logs):
    if len(logs) > 0:
        print("Попередні дії")
        for item in logs:
            print(item)


def ask_first_number():
    return "Введи число, або 'exit' для виходу: "


def ask_operation(pref_num):
    return f"Ваше число: {pref_num}, оберіть операцію (+, -, *, /): "


def ask_second_number(pref_num, operation):
    match operation:
        case "+":
            return f"Додати до {pref_num}: "
        case "-":
            return f"Відняти від {pref_num}: "
        case "*":
            return f"{pref_num} помножити на: "
        case "/":
            return f"{pref_num} розділити на: "
        case _:
            return "Помилка"


def incorrect_input():
    print("Некоректне введення")


def finish_message():
    print("Калькулятор завершив роботу")
