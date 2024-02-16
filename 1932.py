# 정수 삼각형

import sys
n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(i+1):
        dp[i][j] = line[j]

# dp
for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j-1]
        else:
            dp[i][j] += max(dp[i - 1][j - 1], dp[i-1][j])

# for i in range(n):
#     for j in range(n):
#         print(dp[i][j], end=" ")
#     print()

print(max(dp[n-1]))
