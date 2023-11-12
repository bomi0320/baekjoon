# 2×n 타일링 2
def tile(n):
    # base case
    if n == 1:
        return 1
    elif n == 2:
        return 3

    else:
        tileList = [0]*(n+1)
        tileList[1] = 1
        tileList[2] = 3
        for i in range(3, n+1):
            tileList[i] = tileList[i-1] + tileList[i-2]*2
        return tileList[n]


n = int(input())
print(tile(n) % 10007)
