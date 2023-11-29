# 회의실 배정
import sys

n = int(input())
timetable = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    timetable.append([s, e])

timetable.sort(key=lambda x: (x[1], x[0]))

time = 0
count = 0  # 회의의 최대 개수
for t in timetable:
    if t[0] >= time:
        count += 1
        time = t[1]

print(count)
