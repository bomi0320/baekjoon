# 미로 탐색

import sys
from collections import deque

n, m = map(int, input().split())

maze = []
direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]

for _ in range(n):
    maze.append(list(map(int, list(sys.stdin.readline().rstrip()))))

queue = deque()
queue.append((0, 0, 1))

while len(queue) != 0:
    x, y, this_num = queue.popleft()
    for i in range(4):
        next_x = x + direction_x[i]
        next_y = y + direction_y[i]
        if 0 <= next_x < n and 0 <= next_y < m:
            if maze[next_x][next_y] == 1:
                maze[next_x][next_y] = this_num + 1
                queue.append((next_x, next_y, this_num + 1))

print(maze[n-1][m-1])
