def strStr(haystack, needle):
    if len(needle) > len(haystack):
        return -1
    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:
            j = 0
            while j < len(needle):
                if i + j >= len(haystack):
                    break
                if haystack[i + j] == needle[j]:
                    j += 1
                    if j == len(needle):
                        return i
                else:
                    break
        i += 1
    return -1

print(strStr("buuuudbuuuudbuuuud", "buuuut"))