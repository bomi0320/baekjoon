# 행렬
import sys

n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(sys.stdin.readline().strip()))
for _ in range(n):
    b.append(list(sys.stdin.readline().strip()))

c = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            c[i][j] = '1'


def change(arr, a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            if arr[i][j] == '1':
                arr[i][j] = '0'
            else:
                arr[i][j] = '1'


cnt = 0
for i in range(n-3+1):
    for j in range(m-3+1):
        if c[i][j] == '1':
            cnt += 1
            change(c, i, j)

flag = True
for i in range(n):
    for j in range(m):
        if c[i][j] == '1':
            flag = False
    if not flag:
        break

if not flag:
    print(-1)
else:
    print(cnt)






