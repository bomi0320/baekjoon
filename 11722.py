# 가장 긴 감소하는 부분 수열

N = int(input())
A = list(map(int, input().split()))

dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] < A[j]:
            tmp = dp[j] + 1
            if tmp > dp[i]:
                dp[i] = tmp

print(max(dp))
