# 주디와 당근농장

n, r, c = map(int, input().split())
r, c = r-1, c-1

if (r + c) % 2 != 0:  # (i + j)가 홀수인 곳에 v
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 != 0:
                print("v", end="")
            else:
                print(".", end="")
        print()
else:  # (i + j)가 짝수인 곳에 v
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("v", end="")
            else:
                print(".", end="")
        print()
