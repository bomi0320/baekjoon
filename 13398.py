# 연속합 2

n = int(input())
nums = list(map(int, input().split()))

dp = [0 for _ in range(n)]
dp[0] = nums[0]
dp_2 = [0 for _ in range(n)]
dp_2[0] = nums[0]

for i in range(1, n):
    tmp = nums[i]
    dp[i] = max(tmp, dp[i-1] + tmp)
    dp_2[i] = max(dp[i-1], dp_2[i-1] + tmp)

print(max(max(dp), max(dp_2)))


