from typing import List


# class Solution:
#     def trap(self, height: List[int]) -> int:
#         l = 0
#         r = len(height) - 1
#         left_maxes = []
#         right_maxes = []
#         left_max = height[0]
#         for h in height:
#             left_maxes.append(left_max)
#             left_max = max(left_max, h)
#         right_max = height[len(height) - 1]
#         for h in height[::-1]:
#             right_maxes.append(right_max)
#             right_max = max(h, right_max)
#         water_per_item = []
#         right_maxes = right_maxes[::-1]
#         for i, h in enumerate(height):
#             water_per_item.append(min(right_maxes[i], left_maxes[i]) - h)
#
#         res = 0
#         for h in water_per_item:
#             if h > 0:
#                 res += h
#         return res

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height) - 1
        max_l = height[0]
        max_r = height[len(height) - 1]
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                res += max_r - height[r]



        return res


print(Solution().trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
