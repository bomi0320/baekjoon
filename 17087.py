# 숨바꼭질 6

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N, S = map(int, input().split())
A = list(map(int, input().split()))

# 수빈~동생 거리 구하기
distance = [0] * N
for i in range(N):
    distance[i] = abs(S-A[i])

# 거리의 gcd 구하기
d = distance[0]
for i in range(1, N):
    d = get_gcd(d, distance[i])

print(d)
