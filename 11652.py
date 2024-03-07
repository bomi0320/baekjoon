# 카드

import sys

n = int(input())

nums = {}
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num in nums:
        nums[num] += 1
    else:
        nums[num] = 1

max_val = max(nums.values())

tmp = []
for key, value in nums.items():
    if value == max_val:
        tmp.append(key)

tmp.sort()

print(tmp[0])
