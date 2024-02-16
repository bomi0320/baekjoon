# 오르막 수

N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N+1)]

# base case
for i in range(10):
    dp[1][i] = 1
for i in range(N+1):
    dp[i][0] = 1

for i in range(2, N+1):
    for j in range(10):
        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

# for i in range(N+1):
#     for j in range(10):
#         print(dp[i][j], end=" ")
#     print()

print(sum(dp[N]) % 10007)
