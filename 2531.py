# 회전 초밥

import sys

N, d, k, c = map(int, input().split())
sushi = []
for _ in range(N):
    sushi.append(int(sys.stdin.readline().rstrip()))
sushi.extend(sushi[:k-1])

result = 0
for i in range(0, N):
    sub_list = sushi[i:i+k]
    cnt = len(set(sub_list))
    if c not in sub_list:
        cnt += 1
    if cnt > result:
        result = cnt
    if cnt == k + 1:
        break

print(result)
