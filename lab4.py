def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def tokenize(expression):
    tokens = []
    number = ""

    for char in expression:
        if char.isdigit() or char == ".":
            number += char
        else:
            if number:
                tokens.append(number)
                number = ""
            if char in "+-*/^()":
                tokens.append(char)

    if number:
        tokens.append(number)

    return tokens


def infix_to_rpn(expression):
    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    output = []
    stack = []

    tokens = tokenize(expression)

    for token in tokens:
        if is_number(token):
            output.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            if not stack:
                raise ValueError("Помилка: неузгоджені дужки")

            stack.pop()

        else: 
            while (
                stack and stack[-1] != "(" and
                priority.get(stack[-1], 0) >= priority[token]
            ):
                output.append(stack.pop())

            stack.append(token)

    while stack:
        if stack[-1] == "(":
            raise ValueError("Помилка: неузгоджені дужки")
        output.append(stack.pop())

    return output


def calculate_rpn(rpn):
    stack = []

    for token in rpn:
        if is_number(token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a / b)
            elif token == "^":
                stack.append(a ** b)

    return stack[0]


def main():
    expression = input("Введіть математичний вираз: ")

    rpn = infix_to_rpn(expression)
    print("Зворотний польський запис:")
    print(" ".join(rpn))

    result = calculate_rpn(rpn)
    print("Результат обчислення:", result)


if __name__ == "__main__":
    main()
