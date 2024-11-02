# def maxProfit(prices):
#     left = 0
#     right = 1
#     res = 0
#     while right < len(prices):
#         if prices[right] < prices[left]:
#             left = right
#             right += 1
#         else:
#             while right + 1 < len(prices) and prices[right + 1]  > prices[right]:
#                 right += 1
#             res  += prices[right] - prices[left]
#             left = right
#             right += 1
#     return res

# in this solution we don't look for best deal like in previous, but sell/buy every time when price is grow
def maxProfit(prices):
    i = 1
    profit = 0
    while i < len(prices):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
        i += 1
    return profit

print(maxProfit([7,1,5,3,6,7]))