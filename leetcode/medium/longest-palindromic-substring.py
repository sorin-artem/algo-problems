class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r = 0
        table = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s) - i):
                if i <= 1:
                    if s[j] == s[j + i]:
                        table[j][j + i] = 1
                        if res_r - res_l <= j + i - j:
                            res_r = j + i
                            res_l = j
                else:
                    if s[j] == s[j + i] and table[j + 1][j + i - 1] == 1:
                        table[j][j + i] = 1
                        if res_r - res_l <= j + i - j:
                            res_r = j + i
                            res_l = j

        return s[res_l:res_r + 1]


print(Solution().longestPalindrome("aaaabbaa"))
