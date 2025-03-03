class Solution:
    def pivotArray(self, nums, pivot: int):
        smaller = []
        equal = []
        bigger = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                smaller.append(nums[i])
            elif nums[i] == pivot:
                equal.append(nums[i])
            else:
                bigger.append(nums[i])

        return smaller+equal+bigger


print(Solution().pivotArray([9,12,5,10,14,3,10], 10))
