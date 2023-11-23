# 유기농 배추
import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(u, v):
    global M, N
    queue = deque()
    queue.append((u, v))
    visited[u][v] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            y = now[0] + dy[k]
            x = now[1] + dx[k]
            if 0 <= x < M and 0 <= y < N:
                if not visited[y][x]:
                    if A[y][x] == 1:
                        queue.append((y, x))
                        visited[y][x] = True


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    A = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        A[Y][X] = 1

    visited = [[False for _ in range(M)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                if A[i][j] == 1:
                    BFS(i, j)
                    cnt += 1
    print(cnt)
