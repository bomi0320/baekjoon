# 올림픽
import sys

n, k = map(int, input().split())
score = []
for _ in range(n):
    score.append(list(map(int, sys.stdin.readline().split())))

score.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))


if k == score[0][0]:
    print(1)
else:
    rank = 1
    rank_cnt = 1
    last_inf = score[0]

    for i in range(1, n):
        rank_cnt += 1
        current_inf = score[i]
        if last_inf[1] != current_inf[1] or last_inf[2] != current_inf[2] or last_inf[3] != current_inf[3]:
            rank = rank_cnt

        if current_inf[0] == k:
            break

        last_inf = current_inf

    print(rank)
