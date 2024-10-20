# def longestCommonPrefix(strs):
#     first_word = strs[0]
#     prefix = ""
#     for i in range(len(first_word)):
#         letter = ""
#         for word in strs:
#             try:
#                 if first_word[i] == word[i]:
#                     letter = first_word[i]
#                 else:
#                     letter = ""
#                     break
#             except:
#                 letter = ""
#                 break
#         prefix += letter
#         if letter == "":
#             return prefix
#     return prefix


def longestCommonPrefix(strs):
    pref = strs[0]
    pref_len = len(strs[0])
    for s in strs:
        while pref != s[0:pref_len]:
            pref_len -= 1
            if pref_len == 0:
                return ""
            pref = pref[0:pref_len]
    return pref

print(longestCommonPrefix(["accc","accc", "ac"]))
