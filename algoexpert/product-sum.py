def levelSum(item_to_process, level):
    if isinstance(item_to_process, int):
        return item_to_process * level
    for item in item_to_process:
        return levelSum(item, level + 1)




def productSum(array, level=1):
    sum = 0
    for element in array:
        if isinstance(element, int):
            sum += element * level
        else:
            sum += productSum(element, level + 1) * level
    return sum


print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))
# print(productSum([5, 2, [7, -1]]))

