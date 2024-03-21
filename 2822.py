# 점수 계산
import sys

score = []
for i in range(1, 9):
    score.append((int(sys.stdin.readline()), i))

score.sort(reverse=True)

score_sum = 0
score_list = []
for i in range(5):
    score_sum += score[i][0]
    score_list.append(score[i][1])

score_list.sort()

print(score_sum)
print(*score_list)
