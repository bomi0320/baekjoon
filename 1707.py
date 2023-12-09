# 이분 그래프
import sys
sys.setrecursionlimit(10000000)


def DFS(n):
    global isEven
    visited[n] = True
    for i in vertex[n]:
        if not visited[i]:
            check[i] = (check[n] + 1) % 2
            DFS(i)
        elif check[i] == check[n]:
            isEven = False


T = int(input())
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    vertex = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        vertex[u].append(v)
        vertex[v].append(u)

    check = [0] * (V+1)
    visited = [False] * (V+1)
    isEven = True

    for i in range(1, V+1):
        if isEven:
            DFS(i)
        else:
            break

    if isEven:
        print("YES")
    else:
        print("NO")
