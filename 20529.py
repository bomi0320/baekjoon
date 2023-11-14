# 가장 가까운 세 사람의 심리적 거리
from itertools import combinations
import math


def psychical_distance(mbti_list):
    tmp1 = 0
    for i in range(4):
        if mbti_list[0][i] != mbti_list[1][i]:
            tmp1 += 1

    tmp2 = 0
    for i in range(4):
        if mbti_list[0][i] != mbti_list[2][i]:
            tmp2 += 1

    tmp3 = 0
    for i in range(4):
        if mbti_list[1][i] != mbti_list[2][i]:
            tmp3 += 1

    return tmp1 + tmp2 + tmp3


t = int(input())
for _ in range(t):
    n = int(input())
    members = list(input().split())

    if n == 3:
        print(psychical_distance(members))
    elif n >= 33:  # 비둘기집 원리
        print(0)
    else:
        # 3명 뽑기
        combs = combinations(members, 3)
        min_val = math.inf
        for c in combs:
            result = psychical_distance(c)
            if result < min_val:
                min_val = result
        print(min_val)

