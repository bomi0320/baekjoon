# 세탁소 사장 동혁

coins = [25, 10, 5, 1]
result = [0, 0, 0, 0]

T = int(input())
for _ in range(T):
    result = ['0', '0', '0', '0']

    change = int(input())

    while change:
        for i in range(4):
            coin = coins[i]
            if coin > change:
                continue
            result[i] = str(change // coin)
            change = change % coin

    print(" ".join(result))
