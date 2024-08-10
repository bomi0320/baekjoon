# 나머지 합

from collections import Counter
import math

n, m = map(int, input().split())
A = list(map(int, input().split()))

# 구간 합
S = [A[0]]
for i in range(1, n):
    S.append(S[i-1] + A[i])

# 구간 합의 나머지
remainder_of_S = []
result = 0
for i in range(n):
    remainder = S[i] % m
    remainder_of_S.append(remainder)
    if remainder == 0:  # 0부터 i까지의 합의 나머지가 0인 것
        result += 1

counter = Counter(remainder_of_S)

for key, value in counter.items():
    nCr = math.comb(value, 2)
    result += nCr

print(result)



