# 나무 자르기

n, m = map(int, input().split())
A = list(map(int, input().split()))

lo, hi = max(A)-m, max(A)-1

answer = 0
while lo <= hi:
    medium = (lo + hi) // 2
    temp = 0
    for a in A:
        if a > medium:
            temp += (a - medium)
    if temp >= m:
        lo = medium + 1
        answer = medium
    else:
        hi = medium - 1

print(answer)
