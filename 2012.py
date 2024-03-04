# 등수 매기기
import sys

# 입력받기
n = int(input())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

data.sort()  # 오름차순 정렬

result = 0
for i in range(1, n+1):
    result += abs(i - data[i-1])

print(result)
