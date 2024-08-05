# 트리의 지름

import sys
from collections import deque

n = int(input())
A = [[] for _ in range(n + 1)]


def bfs():
    farthest = (0, 0)  # node, distance
    while len(queue) != 0:
        this_node, this_weight = queue.popleft()
        visited[this_node] = True
        if this_weight > farthest[1]:
            farthest = (this_node, this_weight)
        for component_node, component_weight in A[this_node]:
            if not visited[component_node]:
                queue.append((component_node, component_weight + this_weight))
    return farthest


for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    v = line[0]
    for i in range(1, len(line), 2):
        u = line[i]
        if u == -1:
            break
        else:
            weight = line[i+1]
            A[v].append((u, weight))

queue = deque()

# bfs(1): 1번 노드에서 가장 먼 노드 찾기
visited = [False] * (n + 1)
visited[1] = True
for component in A[1]:
    queue.append(component)
farthest_node = bfs()[0]

# bfs(farthest_node)
visited = [False] * (n + 1)
visited[farthest_node] = True
for component in A[farthest_node]:
    queue.append(component)
farthest_distance = bfs()[1]

print(farthest_distance)
