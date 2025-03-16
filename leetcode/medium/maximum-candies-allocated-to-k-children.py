class Solution:
    def maximumCandies(self, candies, k: int) -> int:
        if sum(candies) < k:
            return 0

        l,r = 1, sum(candies) // k

        res = 1
        while l <= r:
            m = (l + r) // 2
            piles = 0
            for i in range(len(candies)):
                if candies[i] >= m:
                    piles += candies[i] // m
                if piles >= k:
                    break
            if piles >= k:
                res = m
                l = m + 1
            else:
                r = m - 1
        return res

print(Solution().maximumCandies([4,7,5], 16))