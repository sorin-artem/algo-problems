from collections import defaultdict


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while len(count) == 3:
                res += len(s) - r
                count[s[l]] -= 1
                if count[s[l]]==0:
                    count.pop(s[l])
                l += 1


        return res



print(Solution().numberOfSubstrings("abcabc"))