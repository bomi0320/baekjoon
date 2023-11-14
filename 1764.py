# 듣보잡
import sys

n, m = map(int, input().split())
list1 = []  # 듣도 못한 사람 명단
result = []  # 듣도 보도 못한 사람 명단

for _ in range(n):
    list1.append(sys.stdin.readline().strip())

list1 = set(list1)

for _ in range(m):
    name = sys.stdin.readline().strip()
    if name in list1:
        result.append(name)

# 출력
result.sort()
print(len(result))
for i in result:
    print(i)
