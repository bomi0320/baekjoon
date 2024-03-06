# 치킨치킨치킨

import sys
import itertools

n, m = map(int, input().split())
preference = []
for _ in range(n):
    preference.append(list(map(int, sys.stdin.readline().split())))

if n <= 3:
    satisfaction = 0
    for p in preference:
        satisfaction += max(p)
    print(satisfaction)

else:
    chicken = [i for i in range(m)]
    nPr = list(itertools.combinations(chicken, 3))

    satisfaction = 0
    for i in nPr:
        first, second, third = i[0], i[1], i[2]
        tmp_satis = 0
        for p in preference:
            tmp_satis += max(p[first], p[second], p[third])

        if tmp_satis > satisfaction:
            satisfaction = tmp_satis

    print(satisfaction)
