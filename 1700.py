# 멀티탭 스케줄링
import math

n, k = map(int, input().split())

elect = list(map(int, input().split()))

multi = []
index = 0
while len(multi) < n and index < k:
    now = elect[index]
    if now not in multi:
        multi.append(now)
    index += 1

result = 0
for i in range(index, k):
    now = elect[i]
    if now not in multi:
        tmp = []
        for m in multi:
            if m in elect[i:k]:
                tmp.append(elect.index(m, i, k))
            else:
                tmp.append(math.inf)
        max_index = tmp.index(max(tmp))
        multi.pop(max_index)
        multi.append(now)
        result += 1

print(result)
