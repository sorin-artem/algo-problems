import math


def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            return mid
        if target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 73))
