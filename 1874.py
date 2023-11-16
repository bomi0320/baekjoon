# 스택 수열
import sys


n = int(input())
nums = []
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

stack = []
now = 0
result = []
flag = False
for i in nums:
    if now < i:
        for j in range(now, i):
            now += 1
            result.append("+")
            stack.append(now)
        result.append("-")
        stack.pop()
    elif stack[-1] == i:
        result.append("-")
        stack.pop()
    else:
        flag = True
        break

if flag:
    print("NO")
else:
    for i in result:
        print(i)




