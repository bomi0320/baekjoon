# 균형잡힌 세상
import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    flag = True
    if sentence == ".":  # 종료조건
        break
    stack = []
    for s in sentence:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']':
            if not stack:
                flag = False
                break
            if stack.pop() != '[':
                flag = False
                break
        elif s == ')':
            if not stack:
                flag = False
                break
            if stack.pop() != '(':
                flag = False
                break
    if stack:
        print("no")
    else:
        if flag:
            print("yes")
        else:
            print("no")
