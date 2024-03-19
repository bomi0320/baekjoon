# 개똥벌레

import sys
import math

n, h = map(int, input().split())
up = [0 for _ in range(h)]
down = [0 for _ in range(h)]

for i in range(n):
    data = int(sys.stdin.readline().strip())
    if i % 2 == 0:  # down
        down[data-1] += 1
    else:  # up
        up[data - 1] += 1

for i in range(h-2, -1, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]

min_val = math.inf
cnt = 0
for i in range(h):
    tmp = up[i] + down[h-i-1]
    if tmp < min_val:
        min_val = tmp
        cnt = 1
    elif tmp == min_val:
        cnt += 1

print(min_val, cnt)




