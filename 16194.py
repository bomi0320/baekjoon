# 카드 구매하기 2
import math

N = int(input())
cards = list(map(int, input().split()))

min_price = [0] * (N+1)
min_price[1] = cards[0]

for cnt in range(2, N+1):
    price = math.inf
    for i in range(0, cnt):
        temp = cards[i] + min_price[cnt-i-1]
        if temp < price:
            price = temp
    min_price[cnt] = price

print(min_price[-1])
