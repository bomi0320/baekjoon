# 신기한 소수
import sys
sys.setrecursionlimit(100000)


def isPrime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)


N = int(input())
DFS(2)
DFS(3)
DFS(5)
DFS(7)

