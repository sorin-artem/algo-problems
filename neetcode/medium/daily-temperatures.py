def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackI = stack.pop()
            res[stackI] = i - stackI
        stack.append((t, i))
    return res


print(dailyTemperatures([30, 38, 30, 36, 35, 40, 28]))
# [1,4,1,2,1,0,0]
