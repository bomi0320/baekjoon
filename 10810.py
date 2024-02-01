# 공 넣기
import sys

N, M = map(int, input().split())
basket = [0] * (N+1)

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for index in range(i, j+1):
        basket[index] = k

for i in range(1, N+1):
    print(basket[i], end=" ")
