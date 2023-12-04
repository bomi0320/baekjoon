# 칵테일
import sys
from collections import deque

N = int(input())
V = [[] for _ in range(N)]
ratio = []
lcm = 1


# 최대 공약수 구하는 함수
def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


for _ in range(N-1):
    a, b, p, q = map(int, sys.stdin.readline().split())
    V[a].append((b, p, q))
    V[b].append((a, q, p))

    # 비율의 최소공배수 구하기
    lcm *= (p * q // gcd(p, q))


ratio = [0] * N

visited = [False] * N
# BFS
queue = deque()
queue.append(0)
visited[0] = True
ratio[0] = lcm
while queue:
    now = queue.popleft()
    for v in V[now]:
        b, p, q = v[0], v[1], v[2]
        if not visited[b]:
            visited[b] = True
            queue.append(b)
            ratio[b] = ratio[now] * q // p


lcm2 = ratio[0]
for i in range(1, N):
    lcm2 = gcd(lcm2, ratio[i])

new_ratio = list(map(lambda x: x//lcm2, ratio))
for i in new_ratio:
    print(i, end=" ")
print()
