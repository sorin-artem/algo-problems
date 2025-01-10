def isAnagram(s, t):
    s_hash = {}
    if len(s) != len(t):
        return False
    for letter in s:
        if letter in s_hash:
            s_hash[letter] += 1
        else:
            s_hash[letter] = 1
    for letter in t:
        if letter not in s_hash:
            return False
        s_hash[letter] -= 1
        if s_hash[letter] < 0:
            return False

    return True

print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))