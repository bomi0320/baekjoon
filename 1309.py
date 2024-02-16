# 동물원
N = int(input())

dp = [0 for i in range(N+1)]

# base case
dp[0] = 1
dp[1] = 3

for i in range(2, N+1):
    dp[i] = (dp[i-1] * 2 + dp[i-2]) % 9901

print(dp[N] % 9901)

