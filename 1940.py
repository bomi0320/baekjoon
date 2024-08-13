# 주몽

n = int(input())
m = int(input())
A = list(map(int, input().split()))

A.sort()

count = 0
left, right = 0, n-1

while left < right:
    temp = A[left] + A[right]
    if temp == m:
        count += 1
        left += 1
        right -= 1
    elif temp > m:
        right -= 1
    else:
        left += 1

print(count)
