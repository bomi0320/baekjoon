# 구간 합 구하기 4
import sys

n, m = map(int, input().split())
num_list = list(map(int, sys.stdin.readline().split()))

# 누적 합 저장
for i in range(1, n):
    num_list[i] += num_list[i-1]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        print(num_list[b-1])
    else:
        print(num_list[b-1]-num_list[a-2])
