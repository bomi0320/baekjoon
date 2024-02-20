# 카잉 달력

import sys
from math import lcm

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    max_year = lcm(M, N)  # M와 N의 최소공배수

    year = x
    flag = False
    while year <= max_year:
        if (year-y) % N == 0:
            print(year)
            flag = True
            break
        year += M

    if not flag:
        print(-1)



