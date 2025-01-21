def cal(s: str):
    cur, res = 0, 0
    sign = 1  # +1 or -1
    stack = []
    for char in s:
        if char.isdigit():
            cur = cur * 10 + int(char)
        elif char in ("+", "-"):
            res += cur * sign
            cur = 0
            if char == "+":
                sign = 1
            elif char == "-":
                sign = -1
        elif char == "(":
            stack.append({"value": res, "sign": sign})
            res = 0
            sign = 1
        elif char == ")":
            prev = stack.pop()
            res += cur * sign
            res *= prev["sign"]
            res += prev["value"]
            cur = 0


    return res + (cur * sign)


print(cal("(-12-(4+5+2)-3)+(6+8)"))
