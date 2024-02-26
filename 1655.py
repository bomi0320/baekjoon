# 가운데를 말해요

import sys
import heapq

n = int(input())

leftHeap = []  # 최대힙
rightHeap = []  # 최소힙

for _ in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and -leftHeap[0] > rightHeap[0]:
        left = heapq.heappop(leftHeap) * (-1)
        right = heapq.heappop(rightHeap)
        heapq.heappush(leftHeap, right * (-1))
        heapq.heappush(rightHeap, left)

    print(leftHeap[0] * -1)
