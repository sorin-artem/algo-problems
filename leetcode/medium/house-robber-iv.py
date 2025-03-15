class Solution:
    def minCapability(self, nums, k: int) -> int:
        l, r = min(nums), max(nums)
        res=0
        def is_valid(capability):
            i=0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count ==k:
                    break
            return count == k
        while l <= r:
            m = (l + r) // 2
            if is_valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res


Solution().minCapability(
    [2,3,5,9], 2)