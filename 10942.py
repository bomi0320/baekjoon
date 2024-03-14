# 팰린드롬?

import sys

n = int(input())
nums = list(map(int, input().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

# S == E 인 경우
for i in range(1, n+1):
    dp[i][i] = 1

# E - S == 1인 경우
for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i+1][i+2] = 1

# E - S > 1인 경우
for i in range(2, n):
    for j in range(1, n-i+1):
        s, e = j, j+i
        if (nums[s-1] == nums[e-1]) and (dp[s+1][e-1] == 1):
            dp[s][e] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s][e])

