from random import random
from typing import List


def rotate(nums: List[int], k: int) -> None:
    # if k is bigger that length
    k = k % len(nums)
    l, r = 0, len(nums) - 1
    while l<r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    l = 0
    r = k - 1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    l = k
    r = len(nums) - 1

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    print(nums)


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
# [7, 6, 5, 4, 3, 2, 1]
# [5, 6, 7, 4, 3, 2, 1]
# [5, 6, 7, 1, 2, 3, 4]