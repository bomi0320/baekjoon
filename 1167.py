# 트리의 지름
import sys
from collections import deque

V = int(input())
A = [[] for _ in range(V+1)]
for _ in range(V):
    inf = list(map(int, sys.stdin.readline().split()))
    vertex = inf[0]
    for i in range(1, len(inf)+1, 2):
        if inf[i] == -1:
            break
        else:
            A[inf[0]].append((inf[i], inf[i+1]))


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        for q in A[now]:
            if not visited[q[0]]:
                queue.append(q[0])
                visited[q[0]] = True
                distance[q[0]] = distance[now] + q[1]


distance = [0]*(V+1)
visited = [False] * (V+1)
BFS(1)

# max 값인 노드 찾기
max_index = 0
for i in range(1, V+1):
    if distance[i] > distance[max_index]:
        max_index = i

distance = [0]*(V+1)
visited = [False] * (V+1)
BFS(max_index)

print(max(distance))
