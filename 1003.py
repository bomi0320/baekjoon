# 피보나치 함수

def fibo(n):
    if n == 0:
        print(1, 0)
        return
    elif n == 1:
        print(0, 1)
        return
    num_of_0 = [0] * (n+1)
    num_of_1 = [0] * (n+1)
    num_of_0[0] = 1
    num_of_1[1] = 1

    for i in range(2, n+1):
        num_of_0[i] = num_of_0[i - 1] + num_of_0[i - 2]
        num_of_1[i] = num_of_1[i - 1] + num_of_1[i - 2]

    print(num_of_0[n], num_of_1[n])


t = int(input())
for _ in range(t):
    n = int(input())
    fibo(n)
