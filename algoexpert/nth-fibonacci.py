def getNthFib(n):
    firstValue = 0
    secondValue = 1
    iterationNumber = 3
    while iterationNumber <= n:
        next = secondValue + firstValue
        firstValue = secondValue
        secondValue = next
        iterationNumber+=1
    return secondValue

print(getNthFib(6))