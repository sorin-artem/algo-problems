def groupAnagrams(strs):
    hash = {}
    for word in strs:
        count = [0] * 26

        for letter in word:
            count[ord(letter) - ord("a")] += 1
        key = tuple(count)
        if key in hash:
            hash[key].append(word)
        else:
            hash[key] = [word]
    return hash.values()

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
