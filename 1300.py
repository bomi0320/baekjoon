# K번째 수

n = int(input())
k = int(input())

start, end = 1, k
result = 0

while start <= end:
    middle = (start + end) // 2
    temp = 0
    for i in range(1, n + 1):
        temp += min(n, middle//i)
    if temp < k:
        start = middle + 1
    else:
        result = middle
        end = middle - 1

print(result)
