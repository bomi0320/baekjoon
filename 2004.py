# 조합 0의 개수

n, m = map(int, input().split())

# nCm = n!/(n-m)!/m! = a!/b!/c!
a, b, c = n, n-m, m


def expo(d, num):
    cnt = 0
    divide = d
    while num // divide > 0:
        cnt += num // divide
        divide *= d
    return cnt


# 5의 지수 구하기
cnt_5 = expo(5, a) - expo(5, b) - expo(5, c)

# 2의 지수 구하기
cnt_2 = expo(2, a) - expo(2, b) - expo(2, c)

print(min(cnt_5, cnt_2))
