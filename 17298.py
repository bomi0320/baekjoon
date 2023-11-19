# 오큰수

n = int(input())
A = list(map(int, input().split()))

stack = [0]
answer = [0]*n
for i in range(1, n):
    now = A[i]
    if now <= A[stack[-1]]:
        stack.append(i)
    else:
        while len(stack) != 0 and now > A[stack[-1]]:
            index = stack.pop()
            answer[index] = now
        stack.append(i)

while len(stack) != 0:
    index = stack.pop()
    answer[index] = -1

for a in answer:
    print(a, end=" ")
