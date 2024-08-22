# 절댓값 힙

from queue import PriorityQueue
import sys

N = int(input())

que = PriorityQueue()

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:  # 추가
        que.put((abs(x), x))
    else:  # 삭제
        if que.empty():
            print(0)
        else:
            print(que.get()[1])
