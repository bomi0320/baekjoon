# 국회의원 선거

import sys
import heapq

n = int(input())

dasom = int(input())
nomi = []
for _ in range(n-1):
    tmp = int(sys.stdin.readline())
    if tmp >= dasom:
        heapq.heappush(nomi, tmp*(-1))  # 최대힙만들기

if n == 1:
    print(0)
elif not len(nomi):
    print(0)
else:
    cnt = 0
    while True:
        max_val = heapq.heappop(nomi) * (-1)

        if max_val < dasom:
            print(cnt)
            break

        # max_val > dasom
        dasom += 1
        max_val -= 1
        cnt += 1
        heapq.heappush(nomi, max_val*(-1))

