# 수들의 합 2

n, m = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
sum_tmp = 0
cnt = 0
while end < n:
    sum_tmp += nums[end]

    if sum_tmp == m:
        cnt += 1
        start += 1
        end = start
        sum_tmp = 0
    elif sum_tmp < m:
        end += 1
    else:  # sum_tmp > m
        start += 1
        end = start
        sum_tmp = 0

print(cnt)
