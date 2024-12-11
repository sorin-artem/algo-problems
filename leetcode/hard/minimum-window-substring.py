from copy import deepcopy


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""

    count, window = {}, {}

    for letter in t:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    have = 0

    # uniq characters from string t
    need = len(count)
    res, res_len = [-1, -1], float('inf')
    l = 0
    for r in range(len(s)):
        letter = s[r]
        window[letter] = 1 + window.get(letter, 0)
        if letter in count and window[letter] == count[letter]:
            have += 1

        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = (r - l + 1)
            window[s[l]] -= 1
            if s[l] in count and window[s[l]] < count[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l: r+1] if res_len != float("inf") else ""


print(minWindow("ADOBECODEBACNC", "ABCC"))
