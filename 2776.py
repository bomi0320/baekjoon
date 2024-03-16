# 암기왕

import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    nums = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline().rstrip())
    targets = list(map(int, sys.stdin.readline().split()))

    for target in targets:
        if target in nums:
            print(1)
        else:
            print(0)
