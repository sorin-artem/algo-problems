from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            target = nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = target + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([target, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1

        return res

print(Solution().threeSum([-2,0,1,1,2]))
