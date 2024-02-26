# 보석 도둑
import sys
import heapq

n, k = map(int, input().split())
gems = []  # 보석
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(gems, [m, v])

bags = []  # 가방
for _ in range(k):
    bag = int(sys.stdin.readline())
    bags.append(bag)
bags.sort()

tmp = []
total = 0
for bag in bags:
    while gems and bag >= gems[0][0]:
        heapq.heappush(tmp, heapq.heappop(gems)[1] * (-1))
    if tmp:
        total += heapq.heappop(tmp) * (-1)
    elif not gems:
        break

print(total)
