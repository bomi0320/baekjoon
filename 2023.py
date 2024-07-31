# 신기한 소수

import sys
sys.setrecursionlimit(10000)


def isPrime(num):
    for i in range(2, int(num/2 + 1)):
        if num % i == 0:
            return False
    return True


def dfs(num):
    if len(str(num)) == n:
        print(num)
        return
    for i in [1, 3, 5, 7, 9]:
        target = num * 10 + i
        if isPrime(target):
            dfs(target)


n = int(input())

for first_num in [2, 3, 5, 7]:
    dfs(first_num)
