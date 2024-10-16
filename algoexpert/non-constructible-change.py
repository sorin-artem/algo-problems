def nonConstructibleChange(coins):
    coins.sort()
    sum = coins[0]
    print(coins[1:])
    for coin in coins[1:]:
        if(coin > sum + 1):
            return sum + 1
        sum += coin
    return sum + 1

nonConstructibleChange()