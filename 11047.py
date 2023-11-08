# 동전 0
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

count = 0
for c in reversed(coins):
    if c > k:
        continue
    else:
        count += k // c
        k = k % c

print(count)
