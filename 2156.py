# 포도주 시식
import sys
n = int(input())
grape = [0 for _ in range(n)]
dp = [0 for _ in range(n)]

for i in range(n):
    grape[i] = int(sys.stdin.readline())

# dp - base case
dp[0] = grape[0]
if n > 1:
    dp[1] = dp[0] + grape[1]
if n > 2:
    dp[2] = max(dp[1], grape[0]+grape[2], grape[1]+grape[2])

# dp
for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2]+grape[i], dp[i-3]+grape[i-1]+grape[i])

print(dp[n-1])
