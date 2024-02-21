# 거스름돈

coins = [500, 100, 50, 10, 5, 1]

money = int(input())
change = 1000 - money

cnt = 0
while change != 0:
    for coin in coins:
        if change < coin:
            continue
        cnt += change // coin
        change %= coin

print(cnt)
