# 타일 채우기
N = int(input())

if N % 2 != 0:
    print(0)
else:
    tmp = N // 2
    dp = [0 for _ in range(tmp+1)]

    # base case
    dp[0] = 1
    dp[1] = 3

    for i in range(2, tmp+1):
        dp[i] = dp[i-1] * dp[1]
        for j in range(0, i-1):
            dp[i] += dp[j] * 2

    print(dp[tmp])
