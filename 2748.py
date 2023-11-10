# 피보나치 수 2
def fibo(n):
    f_lists = [0]*(n+1)
    f_lists[1] = 1

    for i in range(2, n+1):
        f_lists[i] = f_lists[i-1] + f_lists[i-2]

    return f_lists[n]


n = int(input())
print(fibo(n))
