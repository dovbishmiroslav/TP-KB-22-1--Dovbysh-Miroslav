def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("Ділення на 0 неможливе")
    else:
        return res