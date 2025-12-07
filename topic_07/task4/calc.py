from functions import add, sub, mul, div

class Calculator:
    def __init__(self):
        self.pref_num = None
        self.operation = None
        self.is_operate = False
        self.operations = "+-*/"
        self.pref_logs = []

    def check(self):
        if self.pref_logs:
            print("Попередні дії")
            for log in self.pref_logs:
                print(log)

    def calculate(self, val):
        try:
            num = float(val)
            if self.is_operate:
                log1 = str(self.pref_num)
                log2 = str(self.operation)
                log3 = str(num)

                match self.operation:
                    case "+":
                        self.pref_num = add(self.pref_num, num)
                    case "-":
                        self.pref_num = sub(self.pref_num, num)
                    case "*":
                        self.pref_num = mul(self.pref_num, num)
                    case "/":
                        self.pref_num = div(self.pref_num, num)

                log4 = str(self.pref_num)
                final_log = f"{log1} {log2} {log3} = {log4}"

                self.pref_logs.append(final_log)
                if len(self.pref_logs) > 5:
                    self.pref_logs.pop(0)

                self.is_operate = False
            else:
                self.pref_num = num
        except ValueError:
            if val in self.operations and self.pref_num is not None:
                self.operation = val
                self.is_operate = True
            else:
                print("Некоректне введення")

    def run(self):
        while True:
            if self.pref_num is None:
                self.check()
                inp = input("Введи число, або 'exit' для виходу: ")
            elif not self.is_operate:
                self.check()
                inp = input(f"Ваше число: {self.pref_num}, оберіть операцію (+, -, *, /): ")
            elif self.is_operate:
                self.check()
                match self.operation:
                    case "+":
                        inp = input(f"Додати до {self.pref_num}: ")
                    case "-":
                        inp = input(f"Відняти від {self.pref_num}: ")
                    case "*":
                        inp = input(f"{self.pref_num} помножити на: ")
                    case "/":
                        inp = input(f"{self.pref_num} розділити на: ")
                    case _:
                        print("Помилка")
                        continue

            if inp == "exit":
                print("Калькулятор завершив роботу")
                break
            else:
                self.calculate(inp)


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
