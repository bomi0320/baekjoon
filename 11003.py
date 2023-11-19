# 최솟값 찾기
from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))

queue = deque([])
for i in range(N):
    while queue and queue[-1][1] >= nums[i]:
        queue.pop()
    queue.append((i+1, nums[i]))
    if queue[0][0] <= i+1-L:
        queue.popleft()

    print(queue[0][1], end=" ")
