
# def topKFrequent(nums, k):
#     hash={
#
#     }
#     freq = [[] for i in range(len(nums)+ 1)]
#     for num in nums:
#         if num in hash:
#             hash[num] += 1
#         else:
#             hash[num] = 1
#     for num, count in hash.items():
#         freq[count].append(num)
#     res = []
#     for i in range(len(freq) - 1, 0 ,-1):
#         for n in freq[i]:
#             res.append(n)
#         if len(res)==k:
#             return res
#     return res
import heapq
from typing import List


# def topKFrequent(nums, k):
#     hash = {}
#     freq = [[] for i in range(len(nums) + 1)]
#     print(freq)
#     for num in nums:
#         hash[num] = 1 + hash.get(num, 0)
#     for key, value in hash.items():
#         freq[value].append(key)
#     res = []
#     i = len(freq) - 1
#     while len(res) < k:
#         if len(freq[i]) > 0:
#             for num in freq[i]:
#                 res.append(num)
#         i -= 1
#     return res
#
#
def topKFrequent( nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    heap = []
    for num in count.keys():
        heapq.heappush(heap, (count[num], num))
        if len(heap) > k:
            heapq.heappop(heap)

    res = []
    for i in range(k):
        res.append(heapq.heappop(heap)[1])
    return res



print(topKFrequent([3,3,3,3,1,2,2,2,], 2))