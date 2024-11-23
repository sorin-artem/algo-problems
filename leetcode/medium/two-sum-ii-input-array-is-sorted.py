# def twoSum(numbers, target: int):
#     left, right = 0, len(numbers) -1
#     while True:
#         sum = numbers[left] + numbers[right]
#         if sum==target:
#             return [left+1, right+1]
#         if sum < target:
#             left += 1
#         else:
#             right -= 1

def twoSum(nums, target: int):
    left, right = 0, len(nums) -1
    tuples = ((num, i) for i, num in enumerate(nums))
    sorted_tuples = sorted(tuples, key=lambda x: x[0])

    while left < right:
        sum = sorted_tuples[left][0] + sorted_tuples[right][0]
        if sum == target:
            return [sorted_tuples[left][1], sorted_tuples[right][1]]
        elif sum < target:
            left += 1
        else:
            right -= 1


print(twoSum([2,7,11,15], 9))