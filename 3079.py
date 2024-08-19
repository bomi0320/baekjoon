# 입국심사

import sys

n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(sys.stdin.readline()))

min_val = min(A)
lo, hi = min_val, min_val * m

while lo <= hi:
    medium = (lo + hi) // 2
    temp = 0
    for a in A:
        temp += (medium // a)
    if temp >= m:
        answer = medium
        hi = medium - 1
    else:
        lo = medium + 1

print(lo)
