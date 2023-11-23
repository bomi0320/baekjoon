# 단지번호붙이기
import sys
from collections import deque

n = int(input())
A = []
for _ in range(n):
    A.append(list(sys.stdin.readline().strip()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(u, v):
    global cnt
    queue = deque()
    queue.append((u, v))
    visited[u][v] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < n and 0 <= y < n:
                if not visited[x][y]:
                    if A[x][y] == '1':
                        queue.append((x, y))
                        visited[x][y] = True
                        cnt += 1


visited = [[False for _ in range(n)] for _ in range(n)]
house = []
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if A[i][j] == '1':
                cnt = 1
                BFS(i, j)
                house.append(cnt)


house.sort()
print(len(house))
for h in house:
    print(h)
