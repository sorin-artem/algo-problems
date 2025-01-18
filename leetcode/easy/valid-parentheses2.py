def isValid(s):
    stack = []
    parentheses = {")": "(", "}": "{", "]": "["}
    for element in s:
        if element in parentheses:
            if stack and stack[-1] == parentheses[element]:
                stack.pop()
            else:
                return False
        else:
            stack.append(element)

    return len(stack) == 0

print(isValid("(]"))