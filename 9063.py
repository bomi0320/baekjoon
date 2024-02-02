# 대지
x = []
y = []

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

if N == 1:
    print(0)
else:
    print((max(x) - min(x)) * (max(y) - min(y)))
