# Base Conversion

A, B = map(int, input().split())
m = int(input())
num = list(map(int, input().split()))

# A진법 -> 10진법
decimal = 0
for i in range(m):
    decimal += (A**i) * num[m-i-1]

# 10진법 -> B진법
temp = []
while decimal >= B:
    temp.append(decimal % B)
    decimal //= B
temp.append(decimal)

# stack의 성질을 이용해 마지막 원소부터 출력
while temp:
    print(temp.pop(), end=" ")
