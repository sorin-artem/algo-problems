def groupAnagrams(strs):
    res = {}
    for word in strs:
        count = [0] * 26
        for letter in word:
            count[ord(letter) - ord("a")] += 1
        key = tuple(count)
        if key in res:
            res[key].append(word)
        else:
            res[key] = [word]

    return list(res.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))