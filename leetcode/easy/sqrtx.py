def mySqrt(x: int) -> int:
    left = 0
    right = x
    res = 0

    while left <= right:
        mid1 = (right + left) // 2
        mid2 = left + ((right - left) // 2)

        print(f"mid1: {mid1}, mid2: {mid2}")

        if mid1**2 > x:
            right = mid1 - 1
        elif mid1**2 < x:
            left = mid1 + 1
            res = mid1
        else:
            return mid1


print(mySqrt(127))