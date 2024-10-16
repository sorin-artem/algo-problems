def isValid(s: str) -> bool:
    stack = []
    parentheses = {"}": "{", "]": "[", ")": "("}
    for symbol in s:
        if symbol in parentheses:
            if stack and stack[-1] == parentheses[symbol]:
                stack.pop()
            else:
                return False
        else:
            stack.append(symbol)

    return len(stack) == 0

print(isValid("([])"))
