def hasDuplicate(nums) -> bool:
    hash = {}
    for i in range(len(nums)):
        if nums[i] not in hash:
            hash[nums[i]] = True
        else:
            return False
    return True

print(hasDuplicate([1,2,3,3]))