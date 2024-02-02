# 소인수분해
import math

N = int(input())

for i in range(2, N+1):
    while N % i == 0:
        if N == 0:
            break
        N /= i
        print(i)
