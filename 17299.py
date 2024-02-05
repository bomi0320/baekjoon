# 오등큰수
from collections import Counter

N = int(input())
A = list(map(int, input().split()))
F = dict(Counter(A))

stack = []   # index 값을 저장하는 스택
result = [-1] * N
for i in range(N):
    if len(stack) == 0:
        stack.append(i)
    else:
        while True:
            now = A[i]
            top = A[stack[-1]]
            if F[now] > F[top]:
                result[stack[-1]] = now
                stack.pop(-1)
                if len(stack) == 0:
                    stack.append(i)
                    break
            else:
                stack.append(i)
                break

print(*result)
