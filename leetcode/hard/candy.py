def candy(ratings):
    res = [1] * len(ratings)
    for i in range(1, len(ratings)):
        print(ratings[i])
        if ratings[i] > ratings[i-1]:
            res[i] = res[i] + 1
    print(res)
    for i in range(len(ratings) - 2, -1, -1):
        print(ratings[i])
        if ratings[i] > ratings[i + 1]:
            res[i] = max(res[i], res[i + 1] + 1)
    print(res)
    return sum(res)

candy([1,3,2,2,1])

