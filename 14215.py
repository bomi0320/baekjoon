# 세 막대

length = list(map(int, input().split()))
length.sort()
a, b, c = length

if c < a + b:
    print(a + b + c)
else:
    print(a + b + (a + b - 1))
