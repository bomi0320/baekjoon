# N번째 큰 수

import sys

t = int(input())
for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    print(nums[-3])
