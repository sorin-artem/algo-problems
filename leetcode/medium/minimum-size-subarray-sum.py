def minSubArrayLen(target: int, nums):
    res = float("inf")
    left = 0
    sum = 0
    right = 0
    while right < len(nums):
        sum += nums[right]
        while sum >= target:
            if right - left + 1 < res:
                res = right - left + 1
            sum -= nums[left]
            left += 1

        right += 1

    return 0 if res == float("inf") else res


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
