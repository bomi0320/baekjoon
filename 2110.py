# 공유기 설치

import sys

n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(sys.stdin.readline().rstrip()))

houses.sort()

start, end = 1, houses[-1] - houses[0]
while start <= end:
    middle = (start + end) // 2

    cnt = 1
    now = houses[0]
    for i in range(1, n):
        if houses[i] >= now + middle:
            cnt += 1
            now = houses[i]

    if cnt < c:
        end = middle - 1
    else:
        start = middle + 1

print(end)
