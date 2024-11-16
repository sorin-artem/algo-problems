import math


def convert(s, numRows):
    z_letters = numRows + numRows - 2
    rows = len(s)
    if z_letters != 0:
        z_amount = math.ceil(len(s) / z_letters)
        rows = z_amount * z_letters
    matrix = [["" for _ in range(rows)] for _ in range(numRows)]
    letter_index = 0
    column = 0
    row = 0
    if numRows == 1:
        return s
    while letter_index < len(s):
        matrix[row][column]= s[letter_index]
        if column % (numRows - 1) != 0 or row == numRows - 1:
            column += 1
            row -= 1
        else:
            row += 1

        letter_index += 1
    res = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != "":
                res += matrix[i][j]

    return res


print(convert("AB", 1))
print(convert("PAYPALISHIRING", 4))