# 제곱 ㄴㄴ 수
import math

Min, Max = map(int, input().split())
check = [False]*(Max-Min+1)

for i in range(2, int(math.sqrt(Max))+1):
    pow_num = i * i  # 제곱수 4, 9, 16, 25, ...

    start_index = Min//pow_num
    if Min % pow_num != 0:
        start_index += 1
    for j in range(start_index, Max//pow_num + 1):
        c = pow_num * j
        check[c-Min] = True

cnt = 0
for i in check:
    if not i:
        cnt += 1

print(cnt)


