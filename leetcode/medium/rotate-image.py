def rotate(matrix):
    left, right = 0, len(matrix) - 1

    while left < right:
        # iterate all except last
        for i in range(right - left):
            top, bottom = left, right

            # save first
            top_left = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left
        right -= 1
        left += 1
    print(matrix)
#
# rotate([[5, 1, 9, 11],
#               [2, 4, 8, 10],
#               [13, 3, 6, 7],
#               [15, 14, 12, 16]])
rotate([[1,2,3],[4,5,6],[7,8,9]])