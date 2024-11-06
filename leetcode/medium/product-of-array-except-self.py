# with extra space
# def productExceptSelf(nums):
#     prefix = []
#     postfix = []
#     current_prefix = 1
#     current_postfix = 1
#     for i in range(len(nums)):
#         prefix.append(nums[i]*current_prefix)
#         current_prefix *= nums[i]
#         postfix.insert(0, nums[len(nums) - 1 - i]*current_postfix )
#         current_postfix *= nums[len(nums) - 1 - i]
#
#     result = []
#     for i in range(len(nums)):
#         if i == 0:
#             result.append(postfix[i + 1])
#         elif i == len(nums) - 1:
#             result.append(prefix[len(nums) - 2])
#         else:
#             result.append(prefix[i - 1] * postfix[i + 1])
#     return result

def productExceptSelf(nums):
    res = [1] * len(nums)
    i = 0
    prefix = 1
    while i < len(nums) - 1:
        prefix *= nums[i]
        res[i + 1] =  prefix
        i += 1
    postfix = 1
    i = len(nums) - 1
    while i > 0:
        postfix *= nums[i]
        res[i - 1] *= postfix
        i -=1
    # i = len(nums) - 1
    # while i > 1:
    #     res[i-1] = res[i] * nums[i]
    #     i -= 1
    return res


print(productExceptSelf([1,2,3,4]))