# 강의실 배정
import sys
from queue import PriorityQueue

n = int(input())
courses = []
for _ in range(n):
    courses.append(list(map(int, sys.stdin.readline().split())))

courses.sort(key=lambda x: (x[0], x[1]))

# 우선순위 큐 사용
end = PriorityQueue()
end.put(courses[0][1])  # 끝나는 시간을 저장

for course in courses[1:]:
    start_time, end_time = course[0], course[1]
    smallest_in_end = end.get()
    if smallest_in_end > start_time:
        end.put(smallest_in_end)
        end.put(end_time)
    else:
        end.put(end_time)

print(end.qsize())
