# 안테나
import math

n = int(input())
houses = list(map(int, input().split()))

houses.sort()

print(houses[math.ceil(n/2)-1])
