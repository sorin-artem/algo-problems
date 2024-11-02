# Brute Force. Time = O(n^2). Space = O(n)
# def longestConsecutive(nums) -> int:
#     hash_set = set()
#     for num in nums:
#         hash_set.add(num)
#     res = 0
#     for num in nums:
#         seq = 1
#         current = num + 1
#         while current in hash_set:
#             seq += 1
#             current += 1
#         if seq > res:
#             res = seq
#     print(hash_set)
#     return res
from math import trunc

# Time = O(n). Space = O(n)
def longestConsecutive(nums) -> int:
    hash_set = set(nums)
    longest = 0
    for num in nums:
        current_seq = 1
        if num - 1 not in hash_set:
            while num + current_seq in hash_set:
                current_seq += 1
            longest = max(current_seq, longest)
    return longest

print(longestConsecutive([0,3,6]))
