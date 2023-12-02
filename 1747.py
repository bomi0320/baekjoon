# 소수&팰린드롬
import math

N = int(input())
A = [0] * 10000001

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A)))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, len(A), i):
        A[j] = 0


def isPalindrome(d):
    s = str(d)
    a, b = 0, len(s)-1
    while a <= b:
        if s[a] != s[b]:
            return 0
        a += 1
        b -= 1
    return 1


i = N
while True:
    if A[i] != 0:
        if isPalindrome(A[i]):
            print(A[i])
            break
    i += 1

