# 좋다

n = int(input())
A = list(map(int, input().split()))

A.sort()

result = 0
for target_idx in range(n):
    target = A[target_idx]
    i, j = 0, n-1
    while i < j:
        temp = A[i] + A[j]
        if temp == target:
            if i == target_idx:
                i += 1
            elif j == target_idx:
                j -= 1
            else:
                result += 1
                break
        elif temp > target:
            j -= 1
        else:  # temp < target
            i += 1

print(result)
