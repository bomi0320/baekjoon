# 합 구하기
import sys

n = int(input())
a = list(map(int, input().split()))

# 구간 합 구하기
for i in range(1, n):
    a[i] += a[i-1]

a.insert(0, 0)

m = int(input())
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(a[j] - a[i-1])
