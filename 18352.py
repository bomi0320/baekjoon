# 특정 거리의 도시 찾기
import sys
import math
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
city = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    city[A].append(B)

visited = [math.inf for _ in range(N+1)]

# BFS
queue = deque()
queue.append(X)
visited[X] = 0
while queue:
    now = queue.popleft()
    for e in city[now]:
        if visited[e] == math.inf:
            visited[e] = visited[now] + 1
            queue.append(e)

result = []
for i in range(1, N+1):
    if visited[i] == K:
        result.append(i)

if not result:
    print(-1)
else:
    result.sort()
    for e in result:
        print(e)

