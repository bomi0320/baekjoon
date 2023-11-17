# 수 정렬하기
import sys

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()

for i in nums:
    print(i)
