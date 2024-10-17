from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if nums[mid] > target:
        return mid
    else:
        return mid+1

print(searchInsert([2], 5))