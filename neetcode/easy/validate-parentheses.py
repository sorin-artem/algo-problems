def isVallid(s):
    characters = {")": "(",
                  "]": "[",
                  "}": "{"}
    stack = []
    for c in s:
        if not stack or c == "(" or c == "{" or c == "[":
            stack.append(c)
        else:
            if stack[-1] != characters[c]:
                return False
            stack.pop()

    return len(stack) == 0

print(isVallid("([{}])()"))