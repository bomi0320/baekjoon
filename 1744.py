# 수 묶기
import sys
from queue import PriorityQueue

one = 0
zero = 0
plus = PriorityQueue()
minus = PriorityQueue()

N = int(input())
for _ in range(N):
    data = int(sys.stdin.readline())
    if data == 1:
        one += 1
    elif data == 0:
        zero += 1
    elif data > 1:
        plus.put(data * -1)
    else:
        minus.put(data)

result = one

while plus.qsize() > 1:
    result += plus.get() * plus.get()
if plus.qsize() > 0:
    result += plus.get() * -1

while minus.qsize() > 1:
    result += minus.get() * minus.get()
if minus.qsize() > 0 and zero == 0:
    result += minus.get()

print(result)
