# 연결 요소의 개수

import sys

n, m = map(int, input().split())
lines = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    lines[u].append(v)
    lines[v].append(u)

stack = []
visited = [False for _ in range(n+1)]


def dfs():
    while len(stack) != 0:
        target = stack.pop()
        for component in lines[target]:
            if not visited[component]:
                stack.append(component)
                visited[component] = True


num_of_connected_component = 0
for i in range(1, n+1):
    if not visited[i]:
        stack.append(i)
        visited[i] = True
        num_of_connected_component += 1
        dfs()

print(num_of_connected_component)
