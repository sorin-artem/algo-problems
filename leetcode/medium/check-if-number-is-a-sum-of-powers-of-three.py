class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i, cur):
            if cur == n:
                return True
            if cur > n:
                return False
            if 3**i > n:
                return False

            if backtrack(i + 1, cur):
                return True

            return backtrack(i+1, cur + 3**i)
        return backtrack(0,0)


print(Solution().checkPowersOfThree(12))