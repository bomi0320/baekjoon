# 부분수열의 합
from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
for i in range(1, n+1):
    # 조합 만들기
    combs = combinations(nums, i)
    for comb in combs:
        if sum(comb) == s:
            count += 1

print(count)
