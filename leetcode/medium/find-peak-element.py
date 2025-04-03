from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            left_neighbor = nums[m - 1] if m >= 1 else float("-inf")
            right_neighbor = nums[m + 1] if m < len(nums) - 1 else float("-inf")
            if nums[m]>left_neighbor and nums[m] > right_neighbor:
                return m
            if right_neighbor > nums[m]:
                l = m + 1
            else:
                r = m - 1


print(Solution().findPeakElement([3,4,3,2,1]))
