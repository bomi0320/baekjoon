# 제곱수의 합
import math
N = int(input())

square = [i*i for i in range(1, math.floor(math.sqrt(100000))+1)]
dp = [0 for _ in range(100000+1)]

for i in range(1, math.floor(math.sqrt(100000))+1):
    dp[i*i] = 1

if dp[N] == 1:  # 제곱수
    print(1)
else:
    for i in range(2, N+1):
        if dp[i] == 1:
            continue
        s = 0
        min_cnt = math.inf
        while (s < len(square)) and (square[s] < i):
            current = dp[i - square[s]] + 1
            if min_cnt > current:
                min_cnt = current
            s += 1
        dp[i] = min_cnt

    print(dp[N])
