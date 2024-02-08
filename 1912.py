# 연속합
n = int(input())
nums = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = nums[0]

for i in range(1, n):
    current = nums[i]
    dp[i] = max(current, dp[i-1] + current)

print(max(dp))
