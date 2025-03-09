class Solution:
    def numberOfAlternatingGroups(self, colors, k: int) -> int:
        group = 1
        res = 0
        left = 0
        right = 1
        while right < len(colors) + k - 1:
            if colors[right % len(colors)] == colors[(right-1) % len(colors)]:
                group = 1
            else:
                if group != k:
                    group += 1
            if right - left + 1 == k:
                if group == k:
                    res += 1
                left += 1
            right += 1

        return res
print(Solution().numberOfAlternatingGroups([0,1,0,1,0], 3))