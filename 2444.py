# 별 찍기 - 7

N = int(input())

for i in range(1, N+1):   # 1, 2, ..., N
    print(" " * (N - i) + "*" * (2 * (i - 1) + 1))

for i in range(N-1, 0, -1):
    print(" " * (N - i) + "*" * (2 * (i - 1) + 1))
