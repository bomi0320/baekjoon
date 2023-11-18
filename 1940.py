# 주몽
n = int(input())
m = int(input())
mater = list(map(int, input().split()))

mater.sort()

i = 0
j = n-1
sum = mater[i] + mater[j]
cnt = 0

while i < j:
    if sum > m:
        j -= 1
    elif sum < m:
        i += 1
    else:  # sum == n
        i += 1
        j -= 1
        cnt += 1
    sum = mater[i] + mater[j]

print(cnt)
