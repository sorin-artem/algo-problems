def is_between(target, left,right):
    return target > left and target < right

def insert(intervals, newInterval):
    res = []
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    res.append(newInterval)
    return res

# easier to understand for me
def insert2(intervals, newInterval):
    res = []
    i = 0
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)
    res = res + intervals[i:]

    return res

print(insert2([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
# print(insert([[1,3],[6,9]], [2,5]))