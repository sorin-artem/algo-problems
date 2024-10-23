def addBinary(a: str, b: str) -> str:
    i = len(a) - 1
    j = len(b) - 1
    res = ""
    carry = 0
    while i >= 0 or j >= 0:
        sum = carry
        if i >= 0:
            sum += int(a[i])
        if j >= 0:
            sum += int(b[j])
        res = str(sum % 2) + res
        carry = sum // 2
        i -= 1
        j -= 1

    if carry:
        res = "1" + res

    return res


print(addBinary("1010", "1011"))
