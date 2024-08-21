# 좋다

n = int(input())
A = list(map(int, input().split()))

A.sort()

count = 0
for i in range(n):
    target = A[i]
    l, r = 0, n - 1
    while l < r:
        temp = A[l] + A[r]
        if temp == target:
            if l != i and r != i:
                count += 1
                break
            elif l == i:
                l += 1
            else:
                r -= 1
        elif temp > target:
            r -= 1
        else:
            l += 1

print(count)
