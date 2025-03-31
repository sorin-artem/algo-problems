import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = piles[0]
        for i in range(len(piles)):
            max_pile = max(piles[i], max_pile)

        l = 1
        r = max_pile
        min_rate = max_pile
        while l <= r:
            m = (r + l) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                min_rate = min(m, min_rate)
                r = m - 1
            else:
                l = m + 1

        return min_rate


print(Solution().minEatingSpeed([25,10,23,4], 4))
