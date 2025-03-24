from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_end = 0
        for start, end in meetings:
            start = max(start, prev_end + 1)
            length = end - start + 1
            if length > 0:
                days -= length
            prev_end = max(end, prev_end)

        return days


Solution().countDays(10, [[5,7],[1,6],[9,10]])