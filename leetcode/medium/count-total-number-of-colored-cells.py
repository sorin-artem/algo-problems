class Solution:
    def coloredCells(self, n: int) -> int:
        res = 0
        to_color = 1
        for i in range(1,n + 1,1):
            res += to_color
            to_color = i * 4
        return res

print(Solution().coloredCells(2))