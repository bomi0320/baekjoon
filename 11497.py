# 통나무 건너뛰기

import sys

t = int(input())
for _ in range(t):
    n = int(input())
    l_list = list(map(int, sys.stdin.readline().split()))

    l_list.sort()

    max_val = 0
    for i in range(2, n, 2):
        tmp = l_list[i] - l_list[i-2]
        if tmp > max_val:
            max_val = tmp

    for i in range(3, n, 2):
        tmp = l_list[i] - l_list[i - 2]
        if tmp > max_val:
            max_val = tmp

    print(max_val)

