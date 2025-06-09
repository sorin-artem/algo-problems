class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        res_length = float("inf")
        l = 0
        have = 0
        t_count = {}
        cur = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        need = len(t_count)
        for r in range(len(s)):
            cur[s[r]] = 1 + cur.get(s[r], 0)
            if s[r] in t_count and t_count[s[r]] == cur[s[r]]:
                have += 1
            while need == have:
                if res_length > r - l + 1:
                    res = s[l:r + 1]
                    res_length = r - l + 1
                cur[s[l]] -= 1
                if s[l] in t_count and cur[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        return res


# print(Solution().minWindow("OUZODYXAZV", "XYZ"))
# print(Solution().minWindow("aa", "aa"))
print(Solution().minWindow("aaaaaaaaabbbbbcdd", "abcdd"))
