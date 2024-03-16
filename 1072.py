# 게임

x, y = map(int, input().split())
z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    start, end = 1, x
    while start <= end:
        middle = (start + end) // 2
        tmp = ((y + middle) * 100) // (x + middle)
        if tmp == z:
            start = middle + 1
        else:
            end = middle - 1

    print(start)

