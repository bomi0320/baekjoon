# 탑

import sys

n = int(input())

stack = []
result = [0 for _ in range(n)]

heights = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    height = heights[i]

    if len(stack):
        while len(stack) and stack[-1][1] < height:
            stack.pop()
        if len(stack) and stack[-1][1] > height:
            result[i] = stack[-1][0]

    stack.append([i+1, height])  # 현재 높이 스택에 삽입

print(*result)
