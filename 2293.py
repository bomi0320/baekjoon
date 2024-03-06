# 동전 1
import sys

n, k = map(int, input().split())

A = [0 for _ in range(k+1)]
A[0] = 1

for _ in range(n):
    coin = int(sys.stdin.readline().rstrip())

    for i in range(coin, k+1):
        A[i] += A[i-coin]

print(A[-1])
