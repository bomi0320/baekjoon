# 최대 힙

import sys
import heapq

n = int(input())
nums = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not nums:
            print(0)
        else:
            print(heapq.heappop(nums) * (-1))
    else:
        heapq.heappush(nums, x * (-1))
