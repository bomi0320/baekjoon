# 선분 그룹

import sys


n = int(input())
parent = [-1 for _ in range(n)]


def find(a):
    if parent[a] < 0:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    p = find(a)
    q = find(b)
    if p == q:
        return
    parent[p] += parent[q]
    parent[q] = p


def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)


def isCross(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw_abc = ccw(x1, y1, x2, y2, x3, y3)
    ccw_abd = ccw(x1, y1, x2, y2, x4, y4)
    ccw_cda = ccw(x3, y3, x4, y4, x1, y1)
    ccw_cdb = ccw(x3, y3, x4, y4, x2, y2)

    if ccw_abc * ccw_abd == 0 and ccw_cda * ccw_cdb == 0:  # 겹침
        if Ax == Cx:
            if max(Ay, By) < min(Cy, Dy) or max(Cy, Dy) < min(Ay, By):
                return 0
            else:
                return 1
        else:  # Ay == Cy
            if max(Ax, Bx) < min(Cx, Dx) or max(Cx, Dx) < min(Ax, Bx):
                return 0
            else:
                return 1
    elif ccw_abc * ccw_abd <= 0 and ccw_cda * ccw_cdb <= 0:  # 교차
        return 1
    else:
        return 0


lines = []

for i in range(n):
    Ax, Ay, Bx, By = map(int, sys.stdin.readline().split())
    lines.append([Ax, Ay, Bx, By])
    for j in range(0, i):
        Cx, Cy, Dx, Dy = lines[j]

        # 선분 교차 함수
        if isCross(Ax, Ay, Bx, By, Cx, Cy, Dx, Dy):  # isCross==1이면
            union(i, j)

# output
# 1. 그룹의 수
# 2. 가장 크기가 큰 그룹에 속한 선분의 개수
num_of_group = 0
smallest_num = 0
for i in range(len(parent)):
    if parent[i] < 0:
        num_of_group += 1
        if parent[i] < smallest_num:
            smallest_num = parent[i]

print(num_of_group)
print(abs(smallest_num))
