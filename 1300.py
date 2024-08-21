# K번째 수

N = int(input())
K = int(input())

start, end = 1, K
result = 0

while start <= end:
    medium = (start + end) // 2

    temp = 0
    for i in range(1, N+1):
        temp += min(N, medium//i)

    if temp >= K:
        end = medium - 1
        result = medium
    else:
        start = medium + 1

print(result)
