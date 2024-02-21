# 로프
import sys
n = int(input())
ropes = []

for _ in range(n):
    ropes.append(int(sys.stdin.readline()))

ropes.sort(reverse=True)

max_val = 0
for i in range(n):
    now = ropes[i] * (i+1)
    if now > max_val:
        max_val = now

print(max_val)
