# 문자열 집합

import sys
n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(sys.stdin.readline().rstrip())

cnt = 0
for _ in range(m):
    m = sys.stdin.readline().rstrip()
    if m in s:
        cnt += 1

print(cnt)
