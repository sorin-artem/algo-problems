import math


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = ((l + r) // 2)
            row = mid // n
            col =  mid % n
            element = matrix[row][col]
            print(element)
            if element == target:
                return True
            if target > element:
                l = mid + 1
            else:
                r = mid - 1
        return False

print(Solution().searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))