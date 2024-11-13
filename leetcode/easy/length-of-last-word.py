def lengthOfLastWord(s):
    res = 0
    i = len(s) - 1
    while i >= 0:
        if i == len(s) - 1 and s[i] == " ":
            while s[i] == " ":
                i -= 1
        if s[i] == " ":
            return res
        res += 1
        i -= 1
    return res

print(lengthOfLastWord("Hello World "))
