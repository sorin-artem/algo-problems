from copy import deepcopy

# def getLiveNeighbors(i, j, matrix):
#     live_neighbors = []
#     for r in range(-1, 2, 1):
#         for c in range(-1, 2, 1):
#             neighbor_i = i + r
#             neighbor_j = j + c
#             if neighbor_i == i and neighbor_j == j:
#                 continue
#             if neighbor_i < 0 or neighbor_i > len(matrix) - 1:
#                 continue
#             if neighbor_j < 0 or neighbor_j > len(matrix[0]) - 1:
#                 continue
#             if matrix[neighbor_i][neighbor_j] == 1:
#                 live_neighbors.append(1)
#
#     return len(live_neighbors)
#
#
# def gameOfLife(board):
#     rows = len(board)
#     columns = len(board[0])
#     copy = deepcopy(board)
#     for r in range(rows):
#         for c in range(columns):
#             cell = board[r][c]
#             live_neighbors = getLiveNeighbors(r, c, copy)
#             if cell == 1:
#                 if live_neighbors < 2:
#                     board[r][c] = 0
#                 elif live_neighbors == 2 or live_neighbors == 3:
#                     continue
#                 else:
#                     board[r][c] = 0
#             else:
#                 if live_neighbors == 3:
#                     board[r][c] = 1
#     print(board)

def getLiveNeighbors(i, j, matrix):
    live_neighbors_count = 0
    for r in range(-1, 2, 1):
        for c in range(-1, 2, 1):
            neighbor_i = i + r
            neighbor_j = j + c
            if neighbor_i == i and neighbor_j == j:
                continue
            if neighbor_i < 0 or neighbor_i > len(matrix) - 1:
                continue
            if neighbor_j < 0 or neighbor_j > len(matrix[0]) - 1:
                continue
            if matrix[neighbor_i][neighbor_j] == 1 or matrix[neighbor_i][neighbor_j] == 3:
                live_neighbors_count += 1

    return live_neighbors_count

# instead of copping hall matrix we update value with these rules:
# 0 - 0 -> 0
# 1 - 0 -> 1
# 0 - 1 -> 2
# 1 - 1 -> 3
def gameOfLife(board):
    rows = len(board)
    columns = len(board[0])
    for r in range(rows):
        for c in range(columns):
            cell = board[r][c]
            live_neighbors = getLiveNeighbors(r, c, board)
            if cell == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    board[r][c] = 3
                else:
                    board[r][c] = 1
            else:
                if live_neighbors == 3:
                    board[r][c] = 2
    for r in range(rows):
        for c in range(columns):
            cell = board[r][c]
            if cell >= 2:
                board[r][c] = 1
            else:
                board[r][c] = 0
    print(board)

gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])