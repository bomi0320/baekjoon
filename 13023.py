# ABCDE
import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)
check = False


def DFS(v, depth):
    global check
    if depth == 5:
        check = True
        return
    visited[v] = True
    for a in A[v]:
        if not visited[a]:
            DFS(a, depth+1)
    visited[v] = False


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)

for i in range(N):
    if check:
        break
    else:
        DFS(i, 1)

if check:
    print(1)
else:
    print(0)
