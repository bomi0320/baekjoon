# 1, 2, 3 더하기 5
import sys

plus = [[0, 0, 0] for _ in range(100001)]

# base case
plus[1] = [1, 0, 0]
plus[2] = [0, 1, 0]
plus[3] = [1, 1, 1]  # 1+2, 2+1, 3+0 개수

# dp
for i in range(4, 100001):
    plus[i][0] = (plus[i - 1][1] + plus[i - 1][2]) % 1000000009  # 1+?(1로 시작X)
    plus[i][1] = (plus[i - 2][0] + plus[i - 2][2]) % 1000000009  # 2+?(2로 시작X)
    plus[i][2] = (plus[i - 3][0] + plus[i - 3][1]) % 1000000009  # 3+?(3으로 시작X)

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(plus[n]) % 1000000009)
