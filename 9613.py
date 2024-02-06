# GCD 합
import sys


def get_gcd(a, b):
    while True:
        a, b = b, a % b
        if b == 0:
            break
    return a


t = int(input())
for _ in range(t):
    n, *nums = map(int, sys.stdin.readline().split())

    result = 0
    for i in range(n-1):
        for j in range(i+1, n):
            gcd = get_gcd(nums[i], nums[j])
            result += gcd

    print(result)
