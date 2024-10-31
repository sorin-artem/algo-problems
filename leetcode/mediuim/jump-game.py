def canJump(nums) -> bool:
    goal = nums[len(nums) - 1]
    for i in range(len(nums))[::-1]:
        if goal <= nums[i] + i:
            goal = i

    return goal == 0


print(canJump([2, 3, 0, 0, 4]))
