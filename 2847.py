# 게임을 만든 동준이
import sys

n = int(input())
scores = [0 for _ in range(n)]
for i in range(n):
    scores[i] = int(sys.stdin.readline().strip())

cnt = 0
last_level_score = scores[-1]
for i in range(n-2, -1, -1):
    now = scores[i]
    if now >= last_level_score:
        target_score = last_level_score - 1
        cnt += now - target_score
        last_level_score = target_score
    else:
        last_level_score = now

print(cnt)
