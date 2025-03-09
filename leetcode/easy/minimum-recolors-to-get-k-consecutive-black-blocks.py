class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        right = 0
        res = float("inf")
        current = 0
        while right < len(blocks):
            if blocks[right] == "W":
                current += 1

            if right - left + 1 == k:
                res = min(current, res)
                if blocks[left] == "W":
                    current -= 1
                left += 1
            right += 1

        return res


print(Solution().minimumRecolors("WBBWWBBWBW", 7))
