# def isHappy(n):
#     checked = set()
#     digits = list(str(n))
#     print(digits)
#     checked.add("".join(digits))
#     while True:
#         res = 0
#         for element in digits:
#             res += int(element) * int(element)
#         digits = list(str(res))
#         if res == 1:
#             return True
#         if str(res) in checked:
#             return False
#         else:
#             checked.add("".join(digits))
#
#     return False


def isHappy(n):
    checked = set()
    while n not in checked:
        checked.add(n)
        res = 0
        while n:
            digit = n % 10
            res += digit * digit
            n = n // 10
        n = res
        if res == 1:
            return True

    return False

print(isHappy(2))