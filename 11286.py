# 절댓값 힙
import sys
from queue import PriorityQueue

N = int(input())

queue = PriorityQueue()

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:  # 절댓값이 가장 작은 값 출력
        if queue.empty():  # 큐가 비어있을 경우
            print(0)
        else:
            print(queue.get()[1])
    else:  # 배열에 추가
        if num < 0:  # 음수일 경우
            # ex) -1 => 우선순위 0.5
            queue.put((0-num-0.5, num))  # (우선순위, 값)
        else:
            # ex) 1 => 우선순위 1
            queue.put((num, num))
