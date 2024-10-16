def isValidSubsequence(array, sequence):
    arrayIndex = 0
    sequenceIndex = 0
    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex = sequenceIndex+1
            arrayIndex = arrayIndex+1
        else:
            arrayIndex = arrayIndex+1
    return sequenceIndex > len(sequence)

isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])