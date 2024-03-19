# 소수의 연속합

# 소수 구하기
n = 4000001
a = [False, False] + [True] * (n-1)
primes = []
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

N = int(input())
start, end = 0, 0
sum_tmp = primes[0]
cnt = 0
while primes[end] <= N:
    if sum_tmp < N:
        end += 1
        if end == len(primes):
            break
        sum_tmp += primes[end]
    elif sum_tmp == N:
        cnt += 1
        start += 1
        sum_tmp -= primes[start-1]
        end += 1
        if end == len(primes):
            break
        sum_tmp += primes[end]
    else:  # sum_tmp > N
        start += 1
        sum_tmp -= primes[start-1]

print(cnt)
