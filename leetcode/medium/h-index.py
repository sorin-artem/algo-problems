# Time O(n) Space 0(n)
# def hIndex(citations) -> int:
#     n = len(citations)
#     h_indexes = [0] * (n+1)
#     for number in citations:
#         h_indexes[min(number, n)] += 1
#
#     sum = 0
#     for i in range(len(h_indexes))[::-1]:
#         sum += h_indexes[i]
#         if sum >= i:
#             return i
#     return 0

# Time O(n * log(n)) Space O(1)
def hIndex(citations) -> int:
    citations.sort(reverse=True)
    print(citations)
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h = i + 1
        else:
            break

    return h


print(hIndex([3, 0, 6, 3, 5]))
