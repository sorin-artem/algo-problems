def findMinArrowShots(points):
    points.sort()
    count = len(points)
    prev = points[0]
    for i in range(1, len(points)):
        curr = points[i]
        if curr[0] <= prev[1]:
            prev = [curr[0], min(curr[1], prev[1])]
            count -= 1
        else:
            prev = curr

    return count


print(findMinArrowShots([[1, 9], [7, 16], [2, 5], [7, 12], [9, 11], [2, 10], [9, 16], [3, 9], [1, 3]]))
