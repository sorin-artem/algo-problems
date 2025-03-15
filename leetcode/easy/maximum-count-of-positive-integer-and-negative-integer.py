class Solution:
    def maximumCount(self, nums) -> int:
        left = 0
        right = len(nums) - 1
        first_positive = len(nums) - 1
        last_negative = 0

        while left <= right:
            mid = (right + left) // 2
            if nums[mid - 1] <= 0 and nums[mid] >0:
                first_positive = mid
                break
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid - 1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid + 1] >= 0 and nums[mid] < 0:
                last_negative = mid
                break
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        return max(last_negative + 1, len(nums) - first_positive )

# print(Solution().maximumCount([-3,-2,-1,0,0,1,2]))
# print(Solution().maximumCount([-2,-1,-1,1,2,3]))
print(Solution().maximumCount([0,0,0,0]))