from functions import add, sub, mul, div
import operations as msg

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
            msg.incorrect_input()


def work():
    global pref_num, operation, is_operate

    while True:
        if pref_num is None:
            inp = input(msg.ask_first_number())
        elif not is_operate:
            inp = input(msg.ask_operation(pref_num))
        else:
            inp = input(msg.ask_second_number(pref_num, operation))

        if inp == "exit":
            msg.finish_message()
            break
        else:
            calculate(inp)


work()
