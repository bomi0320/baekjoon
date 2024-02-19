# 가장 큰 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))

dp = A[:]

# dp
for i in range(1, N):
    for j in range(0, i):
        if A[i] > A[j]:
            tmp = dp[j] + A[i]
            if tmp > dp[i]:
                dp[i] = tmp

print(max(dp))
