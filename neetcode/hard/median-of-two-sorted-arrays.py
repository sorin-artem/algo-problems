from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(nums2) < len(nums1):
            A, B, = B, A

        l, r = 0, len(A) - 1
        while True:
            m_a = (l + r) // 2
            m_b = half - m_a - 2
            a_left = A[m_a] if m_a >= 0 else float("-inf")
            a_right = A[m_a + 1] if m_a + 1 < len(A) else float("inf")
            b_left = B[m_b] if m_b >= 0 else float("-inf")
            b_right = B[m_b + 1] if m_b + 1 < len(B) else float("inf")

            if a_left <= b_right and b_left <= a_right:
                if total % 2:
                    return min(a_right, b_right)
                else:
                    return (max(a_left, b_left) + min(a_right, b_right)) / 2
            elif a_left > b_right:
                r = m_a - 1
            else:
                l = m_a + 1


print(Solution().findMedianSortedArrays([1, 3], [2, 4]))
