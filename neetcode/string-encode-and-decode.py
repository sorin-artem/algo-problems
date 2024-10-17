from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        if len(s) > 0:
            while len(s) != 0:
                divider_index = 0
                while s[divider_index] != "#":
                    divider_index += 1
                word_length = int(s[:divider_index])
                s = s[divider_index+1:]
                res.append(s[0:word_length])
                s = s[word_length:]
        return res


solution = Solution()

print(solution.encode(["we", "say", ":", "yes", "!@#$%^&*()"]))
print(solution.decode("2#we3#say1#:3#yes10#!@#$%^&*()"))
