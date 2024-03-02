# 주식

import sys

t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    price = list(map(int, sys.stdin.readline().split()))
    price.reverse()

    max_val = price[0]
    result = 0
    for i in range(1, n):
        now = price[i]
        if now == max_val:
            continue
        elif now > max_val:
            max_val = now
        else:
            result += (max_val - now)

    print(result)
