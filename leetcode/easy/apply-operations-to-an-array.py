from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
            i += 1
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        return nums


print(Solution().applyOperations([1, 2, 2, 1, 1, 0, 5, 5,10]))
