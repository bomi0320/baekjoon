# 스택 수열

import sys

num = 1
stack = []
result = []
flag = True

n = int(input())
for _ in range(n):
    target = int(sys.stdin.readline())
    if target >= num:
        while target >= num:
            stack.append(num)
            num += 1
            result.append('+')
        stack.pop()
        result.append('-')
    else:
        top = stack.pop()
        if top > target:
            print("NO")
            flag = False
            break
        result.append('-')

if flag:
    for i in result:
        print(i)
