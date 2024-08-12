# K번째 수

n = int(input())
k = int(input())

start, end = 1, k
result = 0

while start <= end:
    medium = (start + end) // 2
    temp = 0
    for i in range(1, n + 1):
        temp += min(n, medium//i)

    if temp < k:
        start = medium + 1
    else:
        end = medium - 1
        result = medium

print(result)