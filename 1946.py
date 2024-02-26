# 신입 사원
import sys
t = int(input())

for _ in range(t):
    n = int(sys.stdin.readline())
    candi = []

    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        candi.append([a, b])

    candi.sort()
    inter_top = candi[0][1]  # 지금까지 가장 높은 인터뷰 점수
    cnt = 1

    for i in range(1, n):
        if inter_top > candi[i][1]:
            cnt += 1
            inter_top = candi[i][1]

    print(cnt)

