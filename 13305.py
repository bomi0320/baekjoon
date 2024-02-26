# 주유소
n = int(input())
city = list(map(int, input().split()))
oil = list(map(int, input().split()))

min_oil = oil[0]
total = city[0] * min_oil

for i in range(1, n-1):
    if oil[i] < min_oil:
        min_oil = oil[i]
    total += city[i] * min_oil

print(total)
