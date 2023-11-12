# 1, 2, 3 더하기
def add123(n):
    # base case
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        addList = [0]*(n+1)
        addList[1] = 1
        addList[2] = 2
        addList[3] = 4
        for i in range(4, n+1):
            addList[i] = addList[i-1] + addList[i-2] + addList[i-3]

        return addList[n]


t = int(input())
for _ in range(t):
    n = int(input())
    print(add123(n))
