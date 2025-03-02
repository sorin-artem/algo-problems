from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i1, i2 = 0, 0

        res = []
        while i1 < len(nums1) or i2 < len(nums2):
            if i1 < len(nums1) and i2 < len(nums2):
                (id1, val1), (id2, val2) = nums1[i1], nums2[i2]
                if id1 == id2:
                    res.append([id1, val1 + val2])
                    i1 += 1
                    i2 += 1
                elif id1 < id2:
                    res.append([id1, val1])
                    i1 += 1
                else:
                    res.append([id2, val2])
                    i2 += 1
            elif i1 < len(nums1):
                res.append([nums1[i1][0], nums1[i1][1]])
                i1 += 1
            else:
                res.append([nums2[i2][0], nums2[i2][1]])
                i2 += 1

        return res


print(Solution().mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
