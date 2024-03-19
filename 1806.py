# 부분합
import math

n, s = map(int, input().split())
A = list(map(int, input().split()))

start, end = 0, 0
sum_tmp = A[end]
result = math.inf
while end < n:
    if sum_tmp >= s:
        if result > end - start + 1:
            result = end - start + 1
        start += 1
        sum_tmp -= A[start-1]
    elif sum_tmp < s:
        end += 1
        if end == n:
            break
        sum_tmp += A[end]
    else:  # sum_tmp > s
        start += 1
        sum_tmp -= A[start-1]

if result == math.inf:
    print(0)
else:
    print(result)
