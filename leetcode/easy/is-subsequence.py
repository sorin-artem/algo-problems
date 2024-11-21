def isSubsequence(s: str, t: str) -> bool:
    left, right = 0, 0

    while right < len(t):
        if t[right] == s[left]:
            left += 1

        right += 1
        if left == len(s):
            return True

    return False

print(isSubsequence("", "ahbgdc"))