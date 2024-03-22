# 생일

import sys

n = int(input())

# 첫번째 사람
name, d, m, y = input().split()
age = int(d) + int(m)*100 + int(y)*10000

# 첫번째 사람의 정보로 oldest, youngest 변수 초기화하기
oldest = [name, age]
youngest = [name, age]

for _ in range(n-1):
    name, d, m, y = sys.stdin.readline().split()
    age = int(d) + int(m)*100 + int(y)*10000
    if age < oldest[1]:
        oldest[0], oldest[1] = name, age
    elif age > youngest[1]:
        youngest[0], youngest[1] = name, age

print(youngest[0])
print(oldest[0])

