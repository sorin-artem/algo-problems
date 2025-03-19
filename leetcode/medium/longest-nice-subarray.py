class Solution:
    def longestNiceSubarray(self, nums) -> int:
        res = 0
        cur = 0
        l = 0
        for r in range(len(nums)):
            while cur & nums[r]:
                cur = cur ^ nums[l]
                l += 1
            res = max(res, r - l + 1)

            cur = cur | nums[r]

        return res

print(Solution().longestNiceSubarray([1, 3, 8, 48, 10]))
