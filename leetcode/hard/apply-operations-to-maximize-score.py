from heapq import heappop, heappush, heapify
from math import sqrt
from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        MOD = 10**9 + 7
        res = 1

        # Compute prime factorization scores
        prime_scores = []
        for n in nums:
            score = 0
            for f in range(2, int(sqrt(n)) + 1):
                if n % f == 0:
                    score += 1
                    while n % f == 0:
                        n //= f
            if n >= 2:
                score += 1
            prime_scores.append(score)

        # Compute left and right bounds
        left_bound = [-1] * N
        right_bound = [N] * N
        stack = []

        # Monotonic stack to find left bounds
        for i in range(N):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left_bound[i] = stack[-1] if stack else -1
            stack.append(i)

        stack.clear()

        # Monotonic stack to find right bounds
        for i in range(N - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right_bound[i] = stack[-1] if stack else N
            stack.append(i)

        # Max heap based on numbers
        min_heap = [(-n, i) for i, n in enumerate(nums)]
        heapify(min_heap)

        while k > 0:
            n, index = heappop(min_heap)
            n = -n
            score = prime_scores[index]

            left_cnt = index - left_bound[index]
            right_cnt = right_bound[index] - index
            count = left_cnt * right_cnt

            operations = min(count, k)
            res = (res * pow(n, operations, MOD)) % MOD
            k -= operations

        return res
