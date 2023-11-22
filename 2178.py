# 미로 탐색
import sys
from collections import deque

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().strip())))

visited = [[False for _ in range(M)] for _ in range(N)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def BFS(x, y):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < N and 0 <= y < M:
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x, y))


BFS(0, 0)
print(A[N-1][M-1])
