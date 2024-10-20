# def isPalindrome(int) -> bool:
#     string = str(int)
#     left = 0
#     right = len(string) - 1
#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    reversed = 0
    x_copy = x

    while x_copy > 0:
        reversed = (reversed * 10) + (x_copy % 10)
        x_copy = x_copy // 10

    return reversed == x



print(isPalindrome(121))
