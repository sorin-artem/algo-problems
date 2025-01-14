def longest(nums):
    nums_set = set(nums)
    longest = 0
    for n in nums_set:
        if n - 1 not in nums_set:
            new_longest = 1
            while n + new_longest in nums_set:
                new_longest += 1
            longest = max(longest, new_longest)
    return longest


print(longest([100,4,200,1,3,2]))
