# 카드 구매하기

N = int(input())
cards = list(map(int, input().split()))
max_price = [0] * (N+1)
max_price[1] = cards[0]

for cnt in range(2, N+1):
    price = 0
    for i in range(0, cnt):
        temp = cards[i] + max_price[cnt-i-1]
        if temp > price:
            price = temp

    max_price[cnt] = price

print(max_price[-1])


