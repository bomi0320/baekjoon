# 행렬 곱셈 순서
import math
import sys

m = [[-1 for _ in range(501)] for _ in range(501)]


def CMM(matrix, i, j):
    if i == j:
        m[i][j] = 0
    else:
        for diagonal in range(1, n):
            for i in range(1, n-diagonal+1):
                j = i + diagonal

                count = math.inf
                for k in range(i, j):  # k: i~j-1
                    temp = m[i][k] + m[k+1][j] + matrix[i-1]*matrix[k]*matrix[j]
                    if temp < count:
                        count = temp
                m[i][j] = count

    return m[1][n]


n = int(input())
matrix = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if i == n-1:
        matrix.append(a)
        matrix.append(b)
    else:
        matrix.append(a)

# m 초기화
for i in range(n + 1):
    for j in range(n + 1):
        m[i][j] = 0

print(CMM(matrix, 1, n))
