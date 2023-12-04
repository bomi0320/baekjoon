# 동전 2
import sys
import math

n, k = map(int, input().split())
coins = []
for _ in range(n):
    c = int(sys.stdin.readline().strip())
    if c not in coins:
        coins.append(c)
coins.sort()

coinsUsed = [math.inf] * (k+1)
coinsUsed[0] = 0
for cents in range(1, k+1):
    now = math.inf
    least = math.inf
    for coin in coins:
        if coin > cents:
            break
        if coinsUsed[cents-coin] < 0:
            continue
        now = coinsUsed[cents-coin] + 1
        if now < least:
            least = now
    coinsUsed[cents] = least

result = coinsUsed[k]
if result == math.inf:
    print(-1)
else:
    print(result)
