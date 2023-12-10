def solution(land):
    height = len(land)
    width = len(land[0])
    visited = [[False for i in range(width)] for j in range(height)]
    oil = [0 for i in range(width)]
    move_list = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def bfs(i, j):
        count = 1
        queue = [(i, j)]
        visited[i][j] = True
        min_y = j
        max_y = j

        while queue:
            i, j = queue.pop(0)

            min_y = min(min_y, j)
            max_y = max(max_y, j)

            for move in move_list:
                x = i + move[0]
                y = j + move[1]

                if x < 0 or y < 0 or x >= height or y >= width:
                    continue
                elif land[x][y] and not visited[x][y]:
                    count += 1
                    visited[x][y] = True
                    queue.append((x, y))

        for k in range(min_y, max_y + 1):
            oil[k] += count

    for i in range(height):
        for j in range(width):
            if land[i][j] and not visited[i][j]:
                bfs(i, j)

    return max(oil)


land = [
    [1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1],
]
result = solution(land)

print(result)
