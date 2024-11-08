def romanToInt(s: str) -> int:
    elements = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    i = len(s) - 1
    while i >= 0:
        if i == 0:
            result += elements[s[i]]
            i-= 1
            continue
        if elements[s[i]] > elements[s[i - 1]]:
            result += elements[s[i]]
            result -= elements[s[i - 1]]
            i -= 2
        else:
            result += elements[s[i]]
            i-= 1
    return result

print(romanToInt("III"))
