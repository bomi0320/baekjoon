# 최소 스패닝 트리
import sys
from queue import PriorityQueue


def initial(n):
    for i in range(n):
        pt[i] = i


def find(i):
    while pt[i] != i:
        pt[i] = pt[pt[i]]
        i = pt[i]
    return i


def equal(p, q):
    return find(p) == find(q)


def merge(p, q):
    i = find(p)
    j = find(q)
    if i != j:
        pt[i] = j


def kruskal(n, queue):
    initial(n+1)
    sum = 0
    cnt = 0
    while cnt < n-1:
        w, i, j = queue.get()
        p = find(i)
        q = find(j)
        if not equal(p, q):
            merge(p, q)
            sum += w
            cnt += 1

    return sum


queue = PriorityQueue()
V, E = map(int, input().split())
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    queue.put((C, A, B))

pt = [0] * (V+1)

print(kruskal(V, queue))
