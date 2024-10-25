from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 or j >= 0:
        if i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        elif i>=0:
            nums1[k] = nums1[i]
            i -= 1
        elif j>=0:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

l1 = [1, 2, 3, 9, 0, 0, 0, 0]
merge(l1, 4, [2, 5, 6, 8], 4)
print(l1)
