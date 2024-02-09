# 1, 2, 3, 더하기 3

import sys

dp = [0 for _ in range(1000001)]

# base case
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1000000009

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n] % 1000000009)
