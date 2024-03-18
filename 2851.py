# 슈퍼 마리오

import sys

scores = []
for i in range(10):
    scores.append(int(sys.stdin.readline().strip()))

# 누적 합 구하기
gap = abs(scores[0] - 100)
result = scores[0]
for i in range(1, 10):
    tmp = scores[i-1] + scores[i]
    scores[i] = tmp
    gap_tmp = abs(tmp - 100)
    if gap_tmp <= gap:
        gap = gap_tmp
        result = tmp

print(result)
