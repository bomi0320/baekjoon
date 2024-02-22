# 기타줄
import math
import sys

n, m = map(int, input().split())

min_bundle_cost = math.inf
min_unit_cost = math.inf
for _ in range(m):
    b, u = map(int, sys.stdin.readline().split())
    if min_bundle_cost > b:
        min_bundle_cost = b
    if min_unit_cost > u:
        min_unit_cost = u

# 세트로만
num_bundle = (n-1) // 6
min_cost = (num_bundle+1) * min_bundle_cost

# 개별로만
cost = n * min_unit_cost
if min_cost > cost:
    min_cost = cost

# 세트 + 개별
num_unit = (n - 6 * num_bundle)
cost = num_bundle * min_bundle_cost + num_unit * min_unit_cost
if min_cost > cost:
    min_cost = cost

print(min_cost)
