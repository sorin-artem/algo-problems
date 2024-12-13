def spiralOrder(matrix):
    res = []
    elements_count = 0
    rows = len(matrix)
    columns = len(matrix[0])
    top, right, bot, left = 0, columns-1, rows-1, 0
    i, j = 0, 0
    while elements_count < rows * columns:
        while j <= right:
            res.append(matrix[i][j])
            j += 1
            elements_count += 1
        top += 1
        j -= 1
        i += 1
        if elements_count == rows * columns:
            return res
        while i <= bot:
            res.append(matrix[i][j])
            i += 1
            elements_count += 1
        right -= 1
        i -= 1
        j -= 1
        if elements_count == rows * columns:
            return res
        while j >= left:
            res.append(matrix[i][j])
            j -= 1
            elements_count += 1
        bot -= 1
        i -= 1
        j += 1
        if elements_count == rows * columns:
            return res
        while i >= top:
            res.append(matrix[i][j])
            i -= 1
            elements_count += 1
        left += 1
        i += 1
        j += 1
    return res

print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))