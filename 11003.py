# 최솟값 찾기

from collections import deque

N, L = map(int, input().split())
A = list(map(int, input().split()))

que = deque([1])  # index 저장
print(A[0], end=" ")
for i in range(2, N+1):
    now = A[i-1]
    if que and A[que[-1]-1] > now:
        que.pop()
        while que and A[que[-1]-1] > now:
            que.pop()
    que.append(i)
    if que[0] < i - L + 1:
        que.popleft()
    print(A[que[0]-1], end=' ')
