# 최소공배수

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    a, b = A, B
    if A < B:
        A, B = B, A

    while B != 0:
        A, B = B, A % B
    # 최소공약수는 A

    print(A*(a//A)*(b//A))
