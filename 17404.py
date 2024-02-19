# RGB거리 2
import sys
from math import inf

N = int(input())
houses = []
for _ in range(N):
    houses.append(list(map(int, sys.stdin.readline().split())))

result = []

for i in range(3):  # RGB
    dp = [[0 for _ in range(3)] for _ in range(N)]

    dp[0][0], dp[0][1], dp[0][2] = inf, inf, inf
    dp[0][i] = houses[0][i]

    for j in range(1, N):
        dp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + houses[j][0]
        dp[j][1] = min(dp[j - 1][0], dp[j - 1][2]) + houses[j][1]
        dp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + houses[j][2]

    dp[-1][i] = inf

    result.append(min(dp[-1]))


print(min(result))

