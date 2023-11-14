# 기타리스트
import sys


def volumn(n, s, m, v):
    dp = [[] for i in range(n+1)]
    dp[0].append(s)

    for i in range(1, n+1):
        for before in dp[i-1]:
            temp1 = before + v[i]
            temp2 = before - v[i]
            if 0 <= temp1 <= m:
                if temp1 not in dp[i]:
                    dp[i].append(temp1)
            if 0 <= temp2 <= m:
                if temp2 not in dp[i]:
                    dp[i].append(temp2)
        if len(dp[i]) == 0:
            return -1

    return max(dp[n])


N, S, M = map(int, input().split())
V = list(map(int, sys.stdin.readline().strip().split()))
V.insert(0, 0)
print(volumn(N, S, M, V))
