from collections import defaultdict


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def at_least_k(k):
            count = defaultdict(int)
            non_vowel = 0
            res = 0
            l = 0
            for r in range(len(word)):
                if word[r] in {"a", "o", "i", "u", "e"}:
                    count[word[r]] += 1
                else:
                    non_vowel += 1
                while non_vowel >= k and len(count) == 5:
                    res += (len(word) - r)
                    if word[l] in {"a", "o", "i", "u", "e"}:
                        count[word[l]] -= 1
                    else:
                        non_vowel -= 1
                    if count[word[l]]==0:
                        count.pop(word[l])
                    l += 1

            return res

        return at_least_k(k) - at_least_k(k + 1)


print(Solution().countOfSubstrings("ieaouqqieaouqq", 1))
