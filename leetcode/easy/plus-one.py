from typing import List


def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits))[::-1]:
        if digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)

        else:
            digits[i] += 1
            return digits

    return digits


plusOne([9])