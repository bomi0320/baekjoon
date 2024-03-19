# 합이 0인 네 정수

import sys

n = int(input())
A = [0 for _ in range(n)]
B = [0 for _ in range(n)]
C = [0 for _ in range(n)]
D = [0 for _ in range(n)]

for i in range(n):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A[i], B[i], C[i], D[i] = a, b, c, d

ab_dict = {}
for i in range(n):
    for j in range(n):
        tmp = A[i] + B[j]
        if tmp in ab_dict:
            ab_dict[tmp] += 1
        else:
            ab_dict[tmp] = 1

cnt = 0
for i in range(n):
    for j in range(n):
        tmp = (C[i] + D[j]) * (-1)
        if tmp in ab_dict:
            cnt += ab_dict[tmp]

print(cnt)
