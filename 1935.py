# 후위 표기식2
N = int(input())
ex = input()
alpha = []
for _ in range(N):
    alpha.append(int(input()))

stack = []

for e in ex:
    if e.isalpha():
        stack.append(alpha[ord(e)-65])  # ord('A') = 65
    else:
        b = stack.pop()
        a = stack.pop()
        temp = 0
        if e == '+':
            temp = a + b
        elif e == '-':
            temp = a - b
        elif e == '*':
            temp = a * b
        else:  # /
            temp = a / b
        stack.append(temp)

print("{:.2f}".format(stack[0]))
