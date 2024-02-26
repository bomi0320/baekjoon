# 최소 힙

import heapq
import sys

n = int(input())

nums = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not nums:
            print(0)
        else:
            print(heapq.heappop(nums))
    else:
        heapq.heappush(nums, x)


