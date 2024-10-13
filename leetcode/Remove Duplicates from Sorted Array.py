def removeDuplicates(nums):
    left = 1
    right = 1
    while right < len(nums):
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
        right += 1
    print(nums[0:left])
    return len(nums[0:left])

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))