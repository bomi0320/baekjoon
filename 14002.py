# 가장 긴 증가하는 부분 수열 4

N = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

max_val = max(dp)
print(max_val)

nums = []
for i in range(N-1, -1, -1):
    if max_val == 0:
        break
    if dp[i] == max_val:
        max_val -= 1
        nums.append(A[i])

for i in range(len(nums)-1, -1, -1):
    print(nums[i], end=" ")
