def rotateString(s: str, goal: str):
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        if s == goal:
            return True
        s = s[1:] + s[0]

    return False


print(rotateString("abcde", "cdeab"))

