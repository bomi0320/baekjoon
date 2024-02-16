# 스티커
import sys

T = int(input())
for _ in range(T):
    n = int(input())
    sticker = []
    for _ in range(2):
        line = list(map(int, sys.stdin.readline().split()))
        sticker.append(line)

    dp = [[0 for _ in range(n)] for _ in range(2)]

    # base case
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    if n >= 2:
        dp[0][1] = sticker[1][0] + sticker[0][1]
        dp[1][1] = sticker[0][0] + sticker[1][1]

    # dp
    for i in range(2, n):
        dp[0][i] = sticker[0][i]
        dp[0][i] += max(dp[1][i-1], dp[1][i-2])

        dp[1][i] = sticker[1][i]
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][n-1], dp[1][n-1]))
