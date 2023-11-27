# 카드 정렬하기
import sys
from queue import PriorityQueue

N = int(input())
pq = PriorityQueue()

for _ in range(N):
    pq.put(int(sys.stdin.readline().strip()))

if N == 1:
    print(0)
else:
    result = 0
    while pq.qsize() > 1:
        a = pq.get()
        b = pq.get()
        tmp = a + b
        result += tmp
        pq.put(tmp)
    print(result)
