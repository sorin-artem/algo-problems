class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        map_obj = {}
        most_c = 0
        l = 0
        for r in range(len(s)):
            map_obj[s[r]] = 1 + map_obj.get(s[r], 0)
            most_c  = max(most_c, map_obj[s[r]])

            if r - l + 1 - most_c > k:
                map_obj[s[l]] -= 1
                l += 1

            res  = max(res, r - l + 1)

        return res




print(Solution().characterReplacement("AAABBBB", 1))
