# 색종이
import sys
n = int(input())
grid = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            grid[i][j] = 1

result = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] == 1:
            result += 1

print(result)
