# 프린터 큐
from collections import deque
import sys

t = int(input())
for _ in range(t):
    # input
    n, m = map(int, sys.stdin.readline().split())
    num_list = list(map(int, sys.stdin.readline().split()))

    # deque 만들고 데이터 삽입
    queue = deque()
    for i in range(n):
        queue.append((num_list[i], i))  # (우선순위, 인덱스)

    order = 1
    while True:
        if queue[0][0] == max(queue)[0]:  # 큐의 맨 앞 값이 최댓값이면
            if queue[0][1] == m:  # 내가 찾는 인덱스라면 while 종료
                break
            else:  # 내가 찾는 인덱스가 아니라면
                queue.popleft()  # 큐의 맨 앞에 있는 최댓값 삭제
                order += 1
        else:  # 큐의 맨 앞 값이 최댓값이 아니라면
            queue.append(queue.popleft())  # 맨 뒤에 삽입

    print(order)
