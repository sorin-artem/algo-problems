from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        cut = 0
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # left part
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m -1
                else:
                    l = m + 1
            # right part
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


# print(Solution().search([3, 4, 5, 6, 1, 2], 1))
# print(Solution().search( [3,5,6,0,1,2], 4))
# print(Solution().search( [1,3,5], 1))
# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
# print(Solution().search([3,1], 1))
# Example 1
# print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4

# Example 2
# print(Solution().search([3, 4, 5, 6, 1, 2], 1))  # Output: 4
# Example 3
print(Solution().search([6, 7, 0, 1, 2, 3, 4, 5], 3))  # Output: 5