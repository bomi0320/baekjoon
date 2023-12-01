# 거의 소수
import math

A, B = map(int, input().split())
nums = [0] * 10000001

for i in range(2, len(nums)):
    nums[i] = i

# 소수 구하기
for i in range(2, int(math.sqrt(len(nums)))+1):
    if nums[i] == 0:
        continue
    for j in range(i+i, len(nums), i):
        nums[j] = 0

# 거의 소수 구하기
cnt = 0
for i in range(2, 10000001):
    if nums[i] != 0:
        tmp = nums[i]
        while nums[i] <= B/tmp:
            if nums[i] >= A/tmp:
                cnt += 1
            tmp = tmp * nums[i]

print(cnt)
