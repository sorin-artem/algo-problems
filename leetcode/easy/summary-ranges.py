def summaryRanges(nums):
    i = 0
    res = []
    while i < len(nums):
        start = i
        while i < len(nums) - 1  and nums[i] + 1 == nums[i+1]:
            i += 1
        if start != i:
            res.append(f"{nums[start]}->{nums[i]}")
        else:
            res.append(f"{nums[i]}")
        i += 1
    return res

print(summaryRanges([0,1,2,4,5,7]))