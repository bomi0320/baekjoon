# 크게 만들기

n, k = map(int, input().split())
num = list(input())

stack = [num[0]]
for i in range(1, n):
    now = num[i]
    while k and stack and now > stack[-1]:
        stack.pop()
        k -= 1
    stack.append(now)

for i in range(k):  # k가 양수라면 끝에 있는 숫자들 빼줘야 함
    stack.pop()
print("".join(stack))
