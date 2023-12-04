# 한글 LCS
import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

a_len, b_len = len(A), len(B)

L = [[0 for _ in range(b_len+1)] for _ in range(a_len+1)]

for i in range(1, a_len+1):
    for j in range(1, b_len+1):
        if A[i-1] == B[j-1]:
            L[i][j] = L[i-1][j-1] + 1
        else:
            L[i][j] = max(L[i][j-1], L[i-1][j])

print(L[a_len][b_len])
