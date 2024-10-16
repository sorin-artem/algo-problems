def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
    return array


def bubbleSort2(array):
    is_sorting = True
    while True:
        for i in range(len(array)- 1):
            if array[i] > array[i + 1]:
                array[i], array[i+1] = array[i + 1], array[i]
                is_sorting = True
        if not is_sorting:
            break
    return array

print(bubbleSort2([8, 5, 2, 9, 5, 6, 3]))