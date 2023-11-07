# 1로 만들기
import math


def make_to_one(n):
    m_list = [0]*(n+1)
    for i in range(2, n+1):
        div_3, div_2, sub_1 = math.inf, math.inf, math.inf
        if i % 3 == 0:
            div_3 = m_list[i//3] + 1
        if i % 2 == 0:
            div_2 = m_list[i//2] + 1
        sub_1 = m_list[i-1] + 1

        m_list[i] = min(div_3, div_2, sub_1)

    return m_list[n]


n = int(input())
print(make_to_one(n))

