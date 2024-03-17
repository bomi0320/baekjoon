# 두 용액
import math

n = int(input())
data = list(map(int, input().split()))

data.sort()

l, r = 0, n - 1
min_val = math.inf
min_data = [0, 0]
while l < r:
    tmp = data[l] + data[r]

    if abs(tmp) < abs(min_val):
        min_val = tmp
        min_data[0], min_data[1] = data[l], data[r]

    if tmp < 0:
        l += 1
    else:
        r -= 1

print(min_data[0], min_data[1])
