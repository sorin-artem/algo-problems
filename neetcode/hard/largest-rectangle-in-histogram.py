def area(heights):
    stack = []
    res = float("-inf")
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            popped_index, popped_height = stack.pop()
            res = max(res, (i - popped_index) * popped_height)
            start = popped_index
        stack.append((start, h))

    for i, h in stack:
        res = max(res, h * ((len(heights) - i)))
    return res


print(area([7, 1, 7, 2, 2, 4]))
