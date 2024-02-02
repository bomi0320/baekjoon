# 진법 변환 2
N, B = map(int, input().split())

result = []
while N >= B:
    remainder = N % B
    if remainder > 9:
        result.append(chr(remainder + 55))
    else:
        result.append(str(N % B))
    N = N//B

if N > 9:
    result.append(chr(N + 55))
else:
    result.append(str(N))

result.reverse()
print("".join(result))
