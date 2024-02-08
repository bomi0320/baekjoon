# 합분해
N, K = map(int, input().split())

dp = [[0 for _ in range(201)] for _ in range(201)]

# base case
for i in range(201):
    dp[1][i] = 1
for i in range(201):
    dp[i][1] = i

for i in range(1, K+1):
    for j in range(2, N+1):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000000

print(dp[K][N] % 1000000000)
