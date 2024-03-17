# 가장 긴 증가하는 부분 수열 5
import math

n = int(input())
nums = list(map(int, input().split()))

lis = [math.inf]
dp = []
for num in nums:
    if lis[-1] < num:
        lis.append(num)
        dp.append((len(lis)-1, num))
    else:
        l, r = 0, len(lis)
        while l < r:
            m = (l + r) // 2
            if lis[m] < num:
                l = m + 1
            else:
                r = m
        lis[r] = num
        dp.append((r, num))


# 가장 긴 증가하는 부분 수열의 길이를 출력
print(len(lis))

# 정답이 될 수 있는 가장 긴 증가하는 부분 수열을 출력
last_idx = len(lis) - 1
result = []
for i in range(len(dp)-1,  -1, -1):
    if dp[i][0] == last_idx:
        result.append(dp[i][1])
        last_idx -= 1

print(*result[::-1])
