# 선분 교차 2

import sys
Ax, Ay, Bx, By = map(int, sys.stdin.readline().split())
Cx, Cy, Dx, Dy = map(int, sys.stdin.readline().split())


def ccw(x1, y1, x2, y2, x3, y3):
    return (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)


ccw_abc = ccw(Ax, Ay, Bx, By, Cx, Cy)
ccw_abd = ccw(Ax, Ay, Bx, By, Dx, Dy)
ccw_cda = ccw(Cx, Cy, Dx, Dy, Ax, Ay)
ccw_cdb = ccw(Cx, Cy, Dx, Dy, Bx, By)

if ccw_abc * ccw_abd == 0 and ccw_cda * ccw_cdb == 0:  # 겹침
    if Ax == Cx:
        if max(Ay, By) < min(Cy, Dy) or max(Cy, Dy) < min(Ay, By):
            print(0)
        else:
            print(1)
    else:  # Ay == Cy
        if max(Ax, Bx) < min(Cx, Dx) or max(Cx, Dx) < min(Ax, Bx):
            print(0)
        else:
            print(1)
elif ccw_abc * ccw_abd <= 0 and ccw_cda * ccw_cdb <= 0:  # 교차
    print(1)
else:
    print(0)
