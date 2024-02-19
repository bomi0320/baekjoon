# 가장 긴 바이토닉 부분 수열

N = int(input())
A = list(map(int, input().split()))
inc = [1 for _ in range(N)]
dec = [1 for _ in range(N)]

# 증가하는 부분 수열(앞에서부터)
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            tmp = inc[j] + 1
            if tmp > inc[i]:
                inc[i] = tmp

# 감소하는 부분 수열(뒤에서부터)
for i in range(N-2, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            tmp = dec[j] + 1
            if tmp > dec[i]:
                dec[i] = tmp

# 바이토닉 부분 수열
bitonic = [inc[i] + dec[i] for i in range(N)]

print(max(bitonic) - 1)
