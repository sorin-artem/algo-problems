from threading import current_thread


# def longestPeak(array):
#     biggest_peak = 0
#     for i in range(len(array)):
#         if i == 0 or i == len(array) - 1:
#             continue
#         if array[i - 1] < array[i] and array[i + 1] < array[i]:
#             current_peak = 3
#             left = i - 1
#             right = i + 1
#             while left > 0:
#                 if array[left] > array[left - 1]:
#                     current_peak += 1
#                     left -= 1
#                 else:
#                     break
#             while right < len(array) - 1:
#                 if array[right] > array[right + 1]:
#                     current_peak += 1
#                     right += 1
#                 else:
#                     break
#             if current_peak > biggest_peak:
#                 biggest_peak = current_peak
#     return biggest_peak



def longestPeak(array):
    biggest_peak = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] and array[i + 1] < array[i]:
            left = i - 1
            right = i + 1
            while left > 0:
                if array[left] > array[left - 1]:
                    left -= 1
                else:
                    break
            while right < len(array) - 1:
                if array[right] > array[right + 1]:
                    right += 1
                else:
                    break
            current_peak = right - left + 1
            if current_peak > biggest_peak:
                biggest_peak = current_peak
            i = right
        else:
            i += 1

    return biggest_peak


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))