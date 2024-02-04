# 쇠막대기
brackets = input()
stack = []

result = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append('(')
    else:
        if brackets[i-1] == '(':  # raser임
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1

print(result)
