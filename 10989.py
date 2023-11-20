# 수 정렬하기 3
import sys
count = [0]*10001
N = int(input())
for _ in range(N):
    num = int(sys.stdin.readline())
    count[num] += 1

for i in range(10001):
    if count[i] != 0:
        for _ in range(count[i]):
            print(i)
