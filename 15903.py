# 카드 합체 놀이

import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))

heapq.heapify(a)

for i in range(m):
    x = heapq.heappop(a)
    y = heapq.heappop(a)
    tmp = x + y
    heapq.heappush(a, tmp)
    heapq.heappush(a, tmp)

print(sum(a))
