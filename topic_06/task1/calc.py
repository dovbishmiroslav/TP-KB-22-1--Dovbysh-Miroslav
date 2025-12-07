from functions import add, sub, mul, div
import operations as msg

pref_num = None
operation = None
is_operate = False
operations = "+-*/"

log1 = ""
log2 = ""
log3 = ""
log4 = ""

pref_logs = []


def check():
    msg.show_previous_logs(pref_logs)


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

            
            final_log = f"{log1} {log2} {log3}= {log4}"
            pref_logs.append(final_log)

            
            if len(pref_logs) > 5:
                pref_logs.pop(0)

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
    global pref_num, operation, is_operate, pref_logs

    while True:
        check()

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
