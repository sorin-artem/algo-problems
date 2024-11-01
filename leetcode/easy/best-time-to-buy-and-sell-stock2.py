def maxProfit(prices) -> int:
    l, r, res = 0, 0, 0
    while r < len(prices):
        if prices[r] > prices[l]:
            if prices[r] - prices[l] > res:
                res = prices[r] - prices[l]
            r += 1
        else:
            l = r
            r += 1
    return res

print(maxProfit([7,1,5,3,6,1,1,8]))