from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        ops = 0
        values = [val for row in grid for val in row]
        values.sort()

        for value in values:
            if (value - values[0]) % x != 0:
                return -1

        i, j = 0, len(values) - 1
        while i < j:
            ops += (values[j] - values[i]) // x
            i += 1
            j -= 1
        return ops

Solution().minOperations([[2,4],[6,8]], 2)