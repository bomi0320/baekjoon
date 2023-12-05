# solved.ac
import sys
EPS = 1e-9

n = int(input())
if n == 0:
    print(0)
else:
    ect = round(n * 0.15 + EPS)
    grade = []
    for _ in range(n):
        grade.append(int(sys.stdin.readline().strip()))

    grade.sort()

    l = len(grade)
    sum = 0
    for i in range(ect, l-ect):
        sum += grade[i]

    print(round(sum / (l-2*ect) + EPS))
