# 수들의 합 5

n = int(input())

i, j = 1, 1
temp = 1
count = 0

while i <= n and j <= n:
    if temp < n:
        j += 1
        temp += j
    elif temp == n:
        count += 1
        temp -= i
        i += 1
        j += 1
        temp += j
    else:
        temp -= i
        i += 1

print(count)
