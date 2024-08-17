# 나머지 합

n, m = map(int, input().split())
A = list(map(int, input().split()))

S = [0 for _ in range(n)]
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

remainder = [0 for _ in range(m)]
for i in S:
    remainder[i % m] += 1

result = remainder[0]
for i in remainder:
    if i != 0:
        result += i * (i-1) // 2

print(result)
