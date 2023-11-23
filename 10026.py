# 적록색약
import sys
from collections import deque

n = int(input())
A = []
for _ in range(n):
    A.append(list(sys.stdin.readline().strip()))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def BFS(r, c, check):  # check: 0(적록색약 아닌), 1(적록색약)
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0 <= x < n and 0 <= y < n:
                if not visited[x][y]:
                    if check == 0:  # 적록색약 아닌
                        if A[now[0]][now[1]] == A[x][y]:
                            queue.append((x, y))
                            visited[x][y] = True
                    else:  # 적록색약
                        if A[now[0]][now[1]] == 'B' or A[x][y] == 'B':
                            if A[now[0]][now[1]] == 'B' and A[x][y] == 'B':
                                queue.append((x, y))
                                visited[x][y] = True
                        else:
                            queue.append((x, y))
                            visited[x][y] = True


# 적록색약 아닌
visited = [[False for _ in range(n)] for _ in range(n)]
result1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j, 0)
            result1 += 1

# 적록색약
visited = [[False for _ in range(n)] for _ in range(n)]
result2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j, 1)
            result2 += 1

print(result1, result2)
