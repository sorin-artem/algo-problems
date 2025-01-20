from openpyxl.pivot.fields import Number


def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            first = stack.pop()
            second = stack.pop()
            stack.append(first + second)
        elif token == "*":
            first = stack.pop()
            second = stack.pop()
            stack.append(first * second)
        elif token == "-":
            first = stack.pop()
            second = stack.pop()
            stack.append(second - first)
        elif token == "/":
            first = stack.pop()
            second = stack.pop()
            stack.append(int(second / first))
        else:
            token = int(token)
            stack.append(token)

    return stack[0]


print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
