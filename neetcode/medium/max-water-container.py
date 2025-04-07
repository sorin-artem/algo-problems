from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = float("-inf")
        l = 0
        r = len(heights) - 1
        while l < r:
            new_area = (r - l) * min(heights[r], heights[l])
            res = max(new_area, res)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return res


Solution().maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6])
