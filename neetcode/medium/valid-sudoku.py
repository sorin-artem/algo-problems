from collections import defaultdict
from typing import List


# def isValidSudoku(board: List[List[str]]) -> bool:
#     for i in range(len(board)):
#         row_set = set()
#         for j in range(len(board[i])):
#             element = board[i][j]
#             if element != ".":
#                 if element not in row_set:
#                     row_set.add(element)
#                 else:
#                     return False
#     for i in range(len(board)):
#         column_set = set()
#         for j in range(len(board[i])):
#             element = board[j][i]
#             if element != ".":
#                 if element not in column_set:
#                     column_set.add(element)
#                 else:
#                     return False
#     square_sets = [[set() for _ in range(3)] for _ in range(3)]
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             square_i = i // 3
#             square_j = j // 3
#             current_square = square_sets[square_i][square_j]
#             element = board[i][j]
#             if element != ".":
#                 if element not in current_square:
#                     current_square.add(element)
#                 else:
#                     return False
#         print(square_sets)
#     return True

def isValidSudoku(board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  # key = (r /3, c /3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True


board = [["1", "2", ".", ".", "3", ".", ".", ".", "."],
         ["4", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", "9", "1", ".", ".", ".", ".", ".", "3"],
         ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
         [".", ".", ".", "8", ".", "3", ".", ".", "5"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", ".", ".", ".", ".", ".", "2", ".", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "8"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(isValidSudoku(board))
