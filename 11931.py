# 수 정렬하기 4
import sys

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort(reverse=True)

for i in range(n):
    print(nums[i])
