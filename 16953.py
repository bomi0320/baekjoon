# A -> B
a, b = map(int, input().split())

cnt = 0
while b > a:
    if b % 2 == 0:
        b //= 2
    elif b % 10 == 1:
        b //= 10
    else:
        break
    cnt += 1

if a == b:
    print(cnt+1)
else:
    print(-1)
