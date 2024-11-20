def is_alphanumeric(character):
    c_ord = ord(character)
    if c_ord <= ord("9") and c_ord>= ord("0"):
        return True

    return c_ord >= ord("a") and c_ord <= ord("z")

def isPalindrome(s: str) -> bool:
    s_lower = s.lower()
    left = 0
    right = len(s_lower) - 1
    while left < right:
        if not is_alphanumeric(s_lower[left]):
            left += 1
            continue
        if not is_alphanumeric(s_lower[right]):
            right -= 1
            continue
        if s_lower[left] != s_lower[right]:
            return False
        left += 1
        right -= 1
    return True


print(isPalindrome("race a car"))