# 수들의 합 5

n = int(input())

cnt = 1
start_index = 1
end_index = 1
sum = 1
while end_index != n:
    if sum < n:
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:  # sum == n:
        end_index += 1
        sum += end_index
        cnt += 1

print(cnt)
