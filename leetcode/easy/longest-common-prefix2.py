def longestCommonPrefix(strs):
    res = 0
    while res < len(strs[0]):
        current = strs[0][res]
        for word in strs:
            if res >= len(word):
                return strs[0][0:res]

            if word[res] == current:
                continue
            else:
                return strs[0][0:res]
        res += 1
    return strs[0][0:res]


print(longestCommonPrefix(["ab", "a"]))