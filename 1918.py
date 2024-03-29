# 후위 표기식
infix = input()
stack = []
result = ''

for i in infix:
    if i.isalpha():
        result += i
    elif i == '(':
        stack.append('(')
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(i)
    else:  # ')'
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()

while stack:
    result += stack.pop()

print(result)
