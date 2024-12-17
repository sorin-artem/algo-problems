# def setZero(matrix):
#     rows = set()
#     columns = set()
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == 0:
#                 rows.add(i)
#                 columns.add(j)
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if i in rows:
#                 matrix[i][j] = 0
#             if j in columns:
#                 matrix[i][j] = 0
#     print(columns)
#     print(rows)
#     print(matrix)

def setZero(matrix):
    zeroRow = False
    rows = len(matrix)
    columns = len(matrix[0])
    for r in range(rows):
        for c in range(columns):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r == 0:
                    zeroRow = True
                else:
                    matrix[r][0] = 0
    for r in range(1, rows):
        for c in range(1, columns):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for r in range(rows):
            matrix[r][0] = 0

    if zeroRow:
        for c in range(columns):
            matrix[0][c] = 0


    print(matrix)


# setZero([[1,1,1],[1,0,1],[1,1,1]])
setZero([[1,1,1],[1,0,1],[1,1,1]])
