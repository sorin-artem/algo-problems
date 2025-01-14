# hashmap O(n) O(n)
def containsNearbyDuplicate(nums, k):
    elements = {}
    for i, num in enumerate(nums):
        if num in elements and i - elements[num] <= k:
            return True
        elements[num] = i
    return False

# hashmap O(n) O(1)
def containsNearbyDuplicate2(nums, k):
    l = 0
    window = set()
    for r in range(len(nums)):
        if r-l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])

    return False

print(containsNearbyDuplicate2([1,2,3,14,45,1,1], 3))
