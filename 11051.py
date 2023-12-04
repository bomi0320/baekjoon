# 이항 계수 2
N, K = map(int, input().split())

A = [[0 for _ in range(K+1)] for _ in range(N+1)]

# base case
for i in range(N+1):
    A[i][0] = 1
for i in range(K+1):
    A[i][i] = 1

# 다이나믹
for i in range(2, N+1):
    for j in range(1, min(i, K+1)):
        A[i][j] = A[i-1][j-1] + A[i-1][j]

print(A[N][K] % 10007)
