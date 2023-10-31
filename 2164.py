# 카드2
from collections import deque

n = int(input())

queue = deque([i for i in range(1, n+1)])
#print(queue)

while len(queue) != 1:
    queue.popleft()
    if len(queue) == 1:
        break
    queue.append(queue[0])
    queue.popleft()

print(queue[0])
