# 집합의 표현
import sys


# 노드 i와 j를 하나로 합치는 연산
def union(i, j):
    i = find(i)
    j = find(j)
    if i != j:
        parent[j] = i


# 노드 i의 대표 노드 반환
def find(i):
    if i == parent[i]:
        return i
    else:
        parent[i] = find(parent[i])
        return parent[i]


n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    o, a, b = map(int, sys.stdin.readline().split())
    if o == 0:  # union
        union(a, b)
    else:  # 포함돼 있는지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
