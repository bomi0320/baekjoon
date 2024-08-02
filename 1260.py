# DFS와 BFS

import sys
from collections import deque

n, m, v = map(int, input().split())

stack = []
queue = deque()


def dfs():
    while len(stack) != 0:
        target = stack.pop()
        if not visited[target]:
            visited[target] = True
            print(target, end=" ")
            for component in sorted(A[target], reverse=True):
                stack.append(component)


def bfs():
    while len(queue) != 0:
        target = queue.popleft()
        print(target, end=" ")
        for component in sorted(A[target]):
            if not visited[component]:
                visited[component] = True
                queue.append(component)


A = [[] for _ in range(n+1)]

for _ in range(m):
    w, u = map(int, sys.stdin.readline().split())
    A[w].append(u)
    A[u].append(w)

# dfs 실행
visited = [False] * (n+1)
stack.append(v)
dfs()

print()

# bfs 실행
visited = [False] * (n+1)
queue.append(v)
visited[v] = True
bfs()
