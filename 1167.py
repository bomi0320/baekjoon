# 트리의 지름

import sys

n = int(input())
A = [[] for _ in range(n+1)]

for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    v = line[0]
    for i in range(1, len(line), 2):
        if line[i] == -1:
            break
        else:
            u, w = line[i], line[i+1]
            A[v].append((u, w))


def dfs():
    farthest_distance, farthest_node = 0, 0
    while len(stack):
        this_node, this_weight = stack.pop()
        visited[this_node] = True
        if this_weight > farthest_distance:
            farthest_distance = this_weight
            farthest_node = this_node
        for next_node, next_weight in A[this_node]:
            if not visited[next_node]:
                stack.append((next_node, next_weight + this_weight))
    return farthest_distance, farthest_node


stack = []

# dfs(1)
visited = [False] * (n + 1)
for i in A[1]:
    stack.append(i)
visited[1] = True
f_distance, f_node = dfs()

# dfs(f_node)
visited = [False] * (n + 1)
for i in A[f_node]:
    stack.append(i)
visited[f_node] = True
f_distance, f_node = dfs()

print(f_distance)
