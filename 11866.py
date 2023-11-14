# 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
queue = deque([i for i in range(1, n+1)])

print("<", end="")
for i in range(n):
    r = k-1
    if i != n-1:
        queue.rotate(-r)
        print(queue.popleft(), end=", ")
    else:
        queue.rotate(-r)
        print(queue.popleft(), end=">")





