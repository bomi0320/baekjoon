# 스택 수열

import sys

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))

now = 1
stack = []
result = []
flag = True
for number in numbers:
    if number >= now:
        while number >= now:
            stack.append(now)
            now += 1
            result.append('+')
        stack.pop()
        result.append('-')
    else:
        if number == stack[-1]:
            stack.pop()
            result.append('-')
        else:
            flag = False
            break

if not flag:
    print("NO")
else:
    for i in result:
        print(i)
