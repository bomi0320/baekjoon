# 먹을 것인가 먹힐 것인가
import sys

t = int(input())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    a.sort()

    cnt = 0
    for i in b:
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] <= i:
                left = mid + 1
            else:
                right = mid - 1
        cnt += n - left

    print(cnt)
