# ABCDE

import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

people = [[] for _ in range(n)]
visited = [False] * n
flag = False


def dfs(node, depth):
    global flag
    if depth == 5:
        flag = True
        return
    visited[node] = True
    for j in people[node]:
        if not visited[j]:
            dfs(j, depth+1)
    visited[node] = False


for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    people[u].append(v)
    people[v].append(u)

for i in range(n):
    dfs(i, 1)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)
