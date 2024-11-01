def jump(nums) -> int:
    l, r = 0, 0
    res = 0

    while r < len(nums) - 1:
        farthest = 0
        for i in range(l, r+ 1):
            if nums[i] + i> farthest:
                farthest = nums[i] + i
        l = r + 1
        r = farthest
        res += 1
    return res

print(jump([1,2,1,1,1]))
