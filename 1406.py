# 에디터
import sys

left_stack = list(input())
right_stack = []

M = int(input())

for _ in range(M):
    c = sys.stdin.readline().split()
    command = c[0]
    if command == 'L':
        if len(left_stack) != 0:
            element = left_stack.pop()
            right_stack.append(element)
    elif command == 'D':
        if len(right_stack) != 0:
            element = right_stack.pop()
            left_stack.append(element)
    elif command == 'B':
        if len(left_stack) != 0:
            element = left_stack.pop()
    else:  # P
        char = c[1]
        left_stack.append(char)

print("".join(left_stack) + "".join(right_stack[::-1]))
