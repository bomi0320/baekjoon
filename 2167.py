# 2차원 배열의 합

import sys

# input
n, m = map(int, input().split())
arr = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(1, m+1):
        arr[i][j] = line[j-1]

# 누적 합 구하기
for i in range(1, n+1):
    for j in range(1, m+1):
        arr[i][j] = arr[i][j-1] + arr[i-1][j] - arr[i-1][j-1] + arr[i][j]


k = int(input())
for _ in range(k):
    i, j, x, y = map(int, sys.stdin.readline().split())
    print(arr[x][y] - arr[i-1][y] - arr[x][j-1] + arr[i-1][j-1])

