# 소수
import math

M = int(input())
N = int(input())

# 소수 찾기
prime = []
for a in range(M, N+1):
    if a == 1:
        continue
    for b in range(2, math.floor(math.sqrt(a))+1):
        if a % b == 0:  # 소수가 아님
            break
    else:
        prime.append(a)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])
