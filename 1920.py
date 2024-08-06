# 수 찾기

import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

m = int(input())
targets = list(map(int, sys.stdin.readline().split()))


def binary_search(tgt):
    left, right = 0, n-1
    while left <= right:
        median = (left + right) // 2
        if A[median] == tgt:
            return 1
        if target < A[median]:
            right = median - 1
        else:
            left = median + 1
    return 0


for target in targets:
    if binary_search(target):
        print(1)
    else:
        print(0)
