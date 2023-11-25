# 기타 레슨
N, M = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 0

for a in A:
    if a > start:
        start = a
    end += a

while start <= end:
    middle = (start + end)//2
    sum = 0
    cnt = 0
    for i in range(N):
        if sum + A[i] > middle:
            cnt += 1
            sum = 0
        sum += A[i]

    if sum != 0:
        cnt += 1

    if cnt > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)

