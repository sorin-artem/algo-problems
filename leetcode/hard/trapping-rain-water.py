# Time: O(n); Space: O(n)
# def water(height):
#     max_lefts = [0] * len(height)
#     max_rights = [0] * len(height)
#     mins = [0] * len(height)
#     res = [0] * len(height)
#
#     left = 0
#     right = 0
#     for i in range(len(height)):
#         max_lefts[i] = left
#         if height[i] > left:
#             left = height[i]
#     for i in range(len(height) - 1, -1, -1):
#         max_rights[i] = right
#         if height[i] > right:
#              right = height[i]
#         mins[i] = min(max_rights[i], max_lefts[i])
#         res[i] = max(mins[i] - height[i], 0)
#
#
#     return sum(res)

# Time: O(n); Space: O(1)
def water(height):
    left = 0
    right = len(height) - 1
    max_left = height[left]
    max_right = height[right]
    res = 0
    while left < right:
        if max_left <= max_right:
            left += 1
            if max_left < height[left]:
                max_left = height[left]
            res += max_left - height[left]
        else:
            right -= 1
            if max_right < height[right]:
                max_right = height[right]
            res += max_right - height[right]
    return res

print(water([0,1,0,2,1,0,1,3,2,1,2,1]))