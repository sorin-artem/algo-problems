class Solution:
    def isAlpaNum(self, c):
        return (ord(c) <= ord("Z") and ord(c) >= ord("A")) or (ord(c) <= ord("z") and ord(c) >= ord("a")) or (
                    ord(c) <= ord("9") and ord(c) >= ord("0"))

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not self.isAlpaNum(s[l]):
                l += 1
            while l < r and not self.isAlpaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True


print(Solution().isPalindrome(".,"))
