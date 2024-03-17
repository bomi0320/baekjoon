# 가장 긴 증가하는 부분 수열 3
import math

n = int(input())
nums = list(map(int, input().split()))

tmp = [math.inf]
for num in nums:
    if tmp[-1] < num:
        tmp.append(num)
    else:
        l, r = 0, len(tmp)
        while l < r:
            m = (l + r) // 2
            if tmp[m] < num:
                l = m + 1
            else:
                r = m
        tmp[r] = num

print(len(tmp))
