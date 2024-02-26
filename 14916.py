# 거스름돈

n = int(input())

if n % 5 == 0:
    print(n // 5)
else:
    dp = [-1 for _ in range(n+1)]
    if n >= 2:
        dp[2] = 1
    if n >= 5:
        dp[5] = 1
    for i in range(3, n+1):
        if dp[i-2] != -1:
            dp[i] = dp[i-2] + 1
        if i-5 >= 0 and dp[i-5] != -1:
            tmp = dp[i-5] + 1
            if dp[i] > tmp:
                dp[i] = tmp
    print(dp[n])
