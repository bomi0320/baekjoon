# 좋다

n = int(input())
A = list(map(int, input().split()))

A.sort()

count = 0

for t in range(n):
    target = A[t]
    i, j = 0, n-1
    while i < j:
        temp = A[i] + A[j]
        if temp == target:
            if i != t and j != t:
                count += 1
                break
            elif i == t:
                i += 1
            elif j == t:
                j -= 1
        elif temp < target:
            i += 1
        else:
            j -= 1

print(count)

