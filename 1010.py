# 다리 놓기
import sys
import math

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    print(math.comb(m, n))
