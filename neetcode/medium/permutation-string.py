class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)
        need = len(s1_count)

        for i in range(len(s2)):
            cur = 0
            s2_count = {}
            for j in range(i, len(s2)):
                s2_count[s2[j]] = 1 + s2_count.get(s2[j], 0)
                if s1_count.get(s2[j], 0) < s2_count[s2[j]]:
                    break
                if s1_count.get(s2[j]) == s2_count[s2[j]]:
                    cur += 1
                if cur == need:
                    return True

        return False


print(Solution().checkInclusion("abc", "lecabee"))