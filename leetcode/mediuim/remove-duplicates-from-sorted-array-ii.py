from typing import List


# def removeDuplicates(nums: List[int]) -> int:
#     left = 0
#     right = 0
#
#     while right < len(nums):
#         count = 1
#         while right + 1 < len(nums) and nums[right] == nums[right + 1]:
#             right += 1
#             count += 1
#         if count > 2:
#             count = 2
#         for i in range(count):
#             nums[left] = nums[right]
#             left += 1
#         right+= 1
#
#     print(nums)
#     print(left)
#
#     return left

# def removeDuplicates(nums):
#     k = 2
#
#     for i in range(2, len(nums)):
#         if nums[i] != nums[k - 2]:
#             nums[k] = nums[i]
#             k += 1
#     print(nums)
#     return k












def removeDuplicates(nums):
    left = 2
    right = 2
    while right < len(nums):
        if nums[right] != nums[left - 2]:
            nums[left] = nums[right]
            left += 1
        right += 1
    print(nums)
    return left






print(removeDuplicates([1,1,1,2,2,3]))
