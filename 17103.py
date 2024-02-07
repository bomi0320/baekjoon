# 골드바흐 파티션
import sys

# 소수 찾기
prime = [1] * 1000001
prime[0] = 0
prime[1] = 0
for i in range(2, 1000001):
    if prime[i] == 0:
        continue
    for j in range(i*i, 1000001, i):
        prime[j] = 0

T = int(input())
for _ in range(T):
    N = int(sys.stdin.readline())

    result = 0
    for i in range(2, N//2+1):
        if prime[i] and prime[N-i]:
            result += 1

    print(result)
