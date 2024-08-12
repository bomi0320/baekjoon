# 수들의 합 5

n = int(input())

result = 0
start, end = 1, 1

now = 1
while end <= n:
    if now < n:
        end += 1
        now += end
    elif now > n:
        now -= start
        start += 1
    else:  # now == target
        result += 1
        now -= start
        start += 1
        end += 1
        now += end

print(result)
