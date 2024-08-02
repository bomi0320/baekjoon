# 토마토

import sys
from collections import deque

m, n = map(int, input().split())

direction_x = [0, 0, 1, -1]
direction_y = [1, -1, 0, 0]

box = []

for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))


def isZero():
    flag = False
    for r in range(n):
        for c in range(m):
            if box[r][c] == 0:
                flag = True
        if flag:
            break
    if flag:
        return True
    else:
        return False


def ripening():
    time = 1
    queue = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j, 1))

    # bfs
    while len(queue) != 0:
        x, y, time = queue.popleft()
        time += 1
        for k in range(4):
            next_x = x + direction_x[k]
            next_y = y + direction_y[k]
            if 0 <= next_x < n and 0 <= next_y < m:
                if box[next_x][next_y] == 0:
                    box[next_x][next_y] = time
                    queue.append((next_x, next_y, time))

    if isZero():
        return -1
    else:
        return time - 2


if not isZero():
    print(0)
else:
    print(ripening())
