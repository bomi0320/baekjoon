# 버블 소트
import sys

N = int(input())
A = []
for i in range(N):
    A.append((int(sys.stdin.readline()), i))

A.sort()

result = []
for i in range(N):
    result.append(A[i][1]-i)

print(max(result)+1)
