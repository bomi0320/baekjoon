# 세 용액

import math

N = int(input())
data = list(map(int, input().split()))

data.sort()

min_val = math.inf
result = [0, 0, 0]
for i in range(N-2):
    left = i + 1
    right = N - 1
    a = data[i]
    flag = False
    while left < right:
        b, c = data[left], data[right]
        tmp_sum = a + b + c
        if abs(tmp_sum) < min_val:
            min_val = abs(tmp_sum)
            result[0], result[1], result[2] = a, b, c
        if tmp_sum < 0:
            left += 1
        elif tmp_sum > 0:
            right -= 1
        else:  # tmp_sum == 0
            flag = True
            break
    if flag:
        break

print(*result)
