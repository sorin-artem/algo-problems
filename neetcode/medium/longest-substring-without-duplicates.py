class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        l = 0
        r = 0
        res = 0
        while r < len(s):
            if s[r] not in characters:
                characters.add(s[r])
            else:
                while s[r] in characters:
                    characters.remove(s[l])
                    l += 1
                characters.add(s[r])
            res = max(res, r - l + 1)
            r += 1


        return res


print(Solution().lengthOfLongestSubstring("dvdf"))
