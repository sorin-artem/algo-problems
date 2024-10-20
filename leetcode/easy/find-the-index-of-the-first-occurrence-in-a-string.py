def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i+j]!=needle[j]:
                break
            if j == len(needle) - 1:
                return i

    return -1

print(strStr("sadbutsad", "sad"))
print(strStr("sadbutsad", "sa63434d"))