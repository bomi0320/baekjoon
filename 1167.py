# 트리의 지름

import sys

v = int(input())

A = [[] for _ in range(v+1)]
for _ in range(v):
    line = list(map(int, sys.stdin.readline().split()))
    v1 = line[0]
    for i in range(1, len(line), 2):
        v2 = line[i]
        if v2 == -1:
            break
        value = line[i+1]
        A[v1].append((v2, value))


def dfs():
    farthest_distance, farthest_node = 0, 0
    while stack:
        node, weight = stack.pop()
        if weight > farthest_distance:
            farthest_distance = weight
            farthest_node = node
        visited[node] = True
        for next_node, next_weight in A[node]:
            if not visited[next_node]:
                stack.append((next_node, next_weight + weight))
    return farthest_distance, farthest_node


stack = []

# dfs 1
visited = [False] * (v+1)
visited[1] = True
for i in A[1]:
    stack.append(i)
f_distance1, f_node1 = dfs()

# dfs farthest_node
visited = [False] * (v+1)
visited[f_node1] = True
for i in A[f_node1]:
    stack.append(i)
f_distance2, f_node2 = dfs()

print(f_distance2)
