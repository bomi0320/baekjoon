# 하노이탑
import sys
sys.setrecursionlimit(100000)


def hanoi(n, start, temp, end):
    if n == 0:
        return
    else:
        hanoi(n-1, start, end, temp)
        print(start, end)
        hanoi(n-1, temp, start, end)


n = int(input())
count = (2**n)-1
if n <= 20:
    print(count)
    hanoi(n, 1, 2, 3)
else:
    print(count)
