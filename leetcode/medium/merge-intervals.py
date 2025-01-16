def merge(intervals):
    intervals = sorted(intervals, key=lambda i: i[0])
    res = [intervals[0]]
    for start, end in intervals[1:]:
        last_added = res[-1]
        if start <= last_added[1]:
            res[-1] = [last_added[0], max(end, last_added[1])]
        else:
            res.append([start, end])

    return res


print(merge([[1, 5], [2, 4],]))
