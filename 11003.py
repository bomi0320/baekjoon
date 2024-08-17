# 최솟값 찾기

from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

deque = deque()

for i in range(N):
    for j in range(len(deque)-1, -1, -1):
        if deque[j][1] < A[i]:
            break
        else:
            deque.pop()
    deque.append((i, A[i]))
    if deque[0][0] <= i-L:
        deque.popleft()
    print(deque[0][1], end=' ')
