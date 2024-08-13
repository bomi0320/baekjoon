# 나머지 합

n, m = map(int, input().split())
A = list(map(int, input().split()))

# 구간 합 구하기
S = [A[0]]
for i in range(1, n):
    S.append(S[i-1] + A[i])

remainder = [0 for _ in range(m)]
for i in S:
    remainder[i % m] += 1

result = remainder[0]
for i in remainder:
    result += i * (i-1) // 2

print(result)
