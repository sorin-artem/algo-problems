def candy(ratings):
    arr = [1] * len(ratings)
    for i in range(len(ratings))[1::]:
        if ratings[i] > ratings[i - 1]:
            arr[i] = arr[i - 1] + 1
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            arr[i] = max(arr[i], arr[i + 1] + 1)
    return sum(arr)
print(candy([1,0,2]))