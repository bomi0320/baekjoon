# 오큰수

n = int(input())
A = list(map(int, input().split()))

answer = [-1 for _ in range(n)]
stack = [0]  # index 0 append

for i in range(1, n):
    nge = A[i]
    while stack and A[stack[-1]] < nge:
        answer[stack.pop()] = nge
    stack.append(i)

for a in answer:
    print(a, end=" ")
