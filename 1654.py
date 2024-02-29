# 랜선 자르기
import sys

k, n = map(int, input().split())
lan_lines = []
for _ in range(k):
    lan_lines.append(int(sys.stdin.readline().rstrip()))

start, end = 1, max(lan_lines)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lan_lines:
        cnt += i // mid
    if cnt < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)


