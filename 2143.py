# 두 배열의 합
import bisect

t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

A_sum = []
for i in range(n):
    tmp = A[i]
    A_sum.append(tmp)
    for j in range(i+1, n):
        tmp += A[j]
        A_sum.append(tmp)

B_sum = []
for i in range(m):
    tmp = B[i]
    B_sum.append(tmp)
    for j in range(i+1, m):
        tmp += B[j]
        B_sum.append(tmp)

A_sum.sort()
B_sum.sort()

cnt = 0
for i in range(len(A_sum)):
    left = bisect.bisect_left(B_sum, t-A_sum[i])
    right = bisect.bisect_right(B_sum, t - A_sum[i])
    cnt += right - left

print(cnt)
