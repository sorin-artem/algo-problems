import math


def operation(a, b, operator):
    if operator == "+":
        return int(a) + int(b)
    elif operator == "-":
        return int(a) - int(b)
    elif operator == "*":
        return int(a) * int(b)
    elif operator == "/":
        return int(a) / int(b)

def evalRPN(tokens) -> int:
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif token == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b / a))
        elif token == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(token))
    return int(stack[0])
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))