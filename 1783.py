# 병든 나이트

n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    if m < 7:
        print((m+1)//2)
    else:
        print(4)
else:  # n>=3
    if m < 7:
        print(min(4, m))
    else:
        print(m-2)
