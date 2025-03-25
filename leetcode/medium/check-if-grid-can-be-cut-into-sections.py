from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x, y = [], []
        for r in rectangles:
            x.append([r[0], r[2]])
            y.append([r[1], r[3]])

        x.sort()
        y.sort()

        def count(intervals):
            count = 0
            prev_end = -1
            for l, r in intervals:
                if l >= prev_end:
                    count += 1
                prev_end = max(r, prev_end)
            return count

        return max(count(x), count(y)) >= 3


print(Solution().checkValidCuts(4, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
