# 골드바흐의 추측

import sys
max_num = 1000001

numbers = [1] * max_num
numbers[0] = 0
numbers[1] = 0
numbers[2] = 0

for i in range(3, max_num):
    if numbers[i]:
        for j in range(2*i, max_num, i):
            numbers[j] = 0

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    N = n
    a, b = 0, 0
    while n:
        if (numbers[n]) and (numbers[N - n]):
            a, b = N - n, n
            break
        else:
            n -= 1
    print(N, "=", a, "+", b)
