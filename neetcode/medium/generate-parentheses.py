def isValid(s):
    stack= []
    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) == 0 or stack[-1] != "(":
                return False
            stack.pop()
    return len(stack) == 0



def generateParenthesis(n: int):
    res = []

    def dfs(open, close, current):
        if open == close == n:
            res.append("".join(current))
            return
        if open < n:
            dfs(open + 1, close, current + ["("])
        if close < open:
            dfs(open, close + 1, current + [")"])

    dfs(0,0, [])

    return res

print(generateParenthesis(3))