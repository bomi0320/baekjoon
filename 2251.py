# 물통
from collections import deque

bottle_max = list(map(int, input().split()))

visited = [[False for _ in range(201)] for _ in range(201)]
result = [False] * 201

sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]


def BFS():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    result[bottle_max[2]] = True
    while queue:
        now = queue.popleft()
        A = now[0]
        B = now[1]
        C = bottle_max[2] - A - B
        for k in range(6):
            s, r = sender[k], receiver[k]
            next = [A, B, C]
            next[r] += next[s]
            next[s] = 0
            if next[r] >= bottle_max[r]:
                next[s] = next[r] - bottle_max[r]
                next[r] = bottle_max[r]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0], next[1]))
                if next[0] == 0:
                    result[next[2]] = True


BFS()

for i in range(len(result)):
    if result[i]:
        print(i, end=" ")
