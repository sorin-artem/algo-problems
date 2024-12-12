def isValidSudoku(board) -> bool:
    rows = [set() for _ in range(len(board))]
    columns = [set() for _ in range(len(board[0]))]
    squares = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(len(board)):
        for j in range(len(board[i])):
            element = board[i][j]
            current_square = squares[i // 3][j // 3]
            current_row = rows[i]
            current_column = columns[j]
            if element == ".":
                continue
            if element in current_square or element in current_row or element in current_column:
                return False

            current_square.add(element)
            current_row.add(element)
            current_column.add(element)

    return True


print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
