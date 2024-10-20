def maxProfit(prices):
    max = 0
    left = 0
    right = 1
    while right < len(prices):
        if prices[right] < prices[left]:
            left = right
            right += 1
        else:
            new_max = prices[right] - prices[left]
            if new_max > max:
                max = new_max
            right += 1
    return max

print(maxProfit([7,3,5,3,6,9, 1, 9]))