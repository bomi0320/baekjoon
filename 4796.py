# 캠핑

import sys

cnt = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l == 0:
        break
    result = (v // p) * l + min(v % p, l)
    print(f"Case {cnt}: {result}")

    cnt += 1
