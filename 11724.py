# 연결 요소의 개수
import sys
sys.setrecursionlimit(100000)

N, M = map(int, input().split())
matrix = [[] for _ in range(N+1)]
visited = [False] * (N+1)


def DFS(vertex):
    visited[vertex] = True
    for a in matrix[vertex]:
        if not visited[a]:
            DFS(a)


for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    matrix[u].append(v)
    matrix[v].append(u)

result = 0
for i in range(1, N+1):
    if not visited[i]:
        result += 1
        DFS(i)

print(result)
