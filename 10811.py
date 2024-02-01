# 바구니 뒤집기
import sys

N, M = map(int, input().split())
basket = [num for num in range(N+1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    basket[i:j+1] = basket[i:j+1][::-1]

for index in range(1, N+1):
    print(basket[index], end=" ")

