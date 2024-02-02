# 알고리즘 수업 - 알고리즘의 수행 시간 6

n = int(input())

result = 0
for i in range(1, n-1):
    result += (i*(i+1)//2)
print(result)
print(3)
