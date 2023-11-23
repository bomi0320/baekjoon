# 바이러스
import sys
from collections import deque

V = int(input())
A = [[] for _ in range(V+1)]
E = int(input())
for _ in range(E):
    u, v = map(int, sys.stdin.readline().split())
    A[u].append(v)
    A[v].append(u)


def BFS(s):
    global cnt
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1


visited = [False] * (V+1)
cnt = 0
BFS(1)
print(cnt)
