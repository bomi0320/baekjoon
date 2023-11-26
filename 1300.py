# K번째 수

N = int(input())
k = int(input())

start = 1
end = k
result = -1

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in range(1, N+1):
        if mid // i > N:
            tmp += N
        else:
            tmp += mid // i
    if tmp < k:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)
