# 최대공약수

def gdc(a, b):
    while b != 0:
        a, b = b, a % b
    print('1'*a)


n, m = map(int, input().split())
gdc(n, m)
