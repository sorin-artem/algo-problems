def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    sizes.sort()
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    current_river_size = 0
    # stack
    nodes_to_explore = [[i, j]]
    while len(nodes_to_explore):
        current_node = nodes_to_explore.pop()
        i = current_node[0]
        j = current_node[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        current_river_size += 1
        unvisited_neighbors = get_unvisited_neighbors(i, j, matrix, visited)
        for neighbor in unvisited_neighbors:
            nodes_to_explore.append(neighbor)
    if current_river_size>=1:
        sizes.append(current_river_size)

def get_unvisited_neighbors(i, j, matrix, visited):
    unvisited_neighbors = []
    if i > 0 and not visited[i-1][j]:
        unvisited_neighbors.append([i-1, j])
    if j > 0 and not visited[i][j-1]:
        unvisited_neighbors.append([i, j-1])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_neighbors.append([i + 1, j])
    if j < len(matrix[i]) - 1 and not visited[i][j+1]:
        unvisited_neighbors.append([i, j + 1])
    return unvisited_neighbors


print(riverSizes([
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 0, 1, 1]
]))
