# ABCDE

import sys

n, m = map(int, input().split())
A = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)


def dfs(node, depth):
    global flag
    if depth == 5:
        flag = True
        return
    visited[node] = True
    for friend in A[node]:
        if not visited[friend]:
            dfs(friend, depth+1)
    visited[node] = False


flag = False
for i in range(n):
    visited = [False] * n
    dfs(i, 1)  # node, depth
    if flag:
        break

if flag:
    print(1)
else:
    print(0)
