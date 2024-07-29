# 다각형의 면적

import sys

n = int(input())
points = []
for _ in range(n):
    points.append(list(map(int, sys.stdin.readline().split())))


# x1, y1 = 0, 0(원점)
def ccw(x2, y2, x3, y3):
    return x2*y3 - x3*y2


sum_of_area = 0
for i in range(n):
    Ax, Ay = points[i][0], points[i][1]
    j = (i+1) % n
    Bx, By = points[j][0], points[j][1]
    sum_of_area += ccw(Ax, Ay, Bx, By)

print(abs(sum_of_area) / 2)
