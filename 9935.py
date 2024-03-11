# 문자열 폭발

s = list(input())
explosion = list(input())

l = len(s)  # 문자열의 길이
explo_l = len(explosion)  # 폭발 문자열의 길이

stack = []  # 스택
for i in range(l):
    stack.append(s[i])  # 스택에 push
    stack_l = len(stack)  # 스택의 길이

    if stack[stack_l-explo_l: stack_l] == explosion:  # 폭발 문자열이면
        for _ in range(explo_l):
            stack.pop()  # 스택에서 push

# 결과 출력
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
