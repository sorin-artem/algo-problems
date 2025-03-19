class Solution:
    def minOperations(self, nums) -> int:
        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                res += 1
                for j in range(i, i+3, 1):
                    if nums[j] == 1:
                        nums[j] = 0
                    else:
                        nums[j] = 1

        for n in nums:
            if n == 0:
                return -1
        return res