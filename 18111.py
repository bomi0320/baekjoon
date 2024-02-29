# 마인크래프트
import sys
import math

n, m, b = map(int, input().split())

height_dic = {}
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for i in line:
        if i in height_dic:
            height_dic[i] += 1
        else:
            height_dic[i] = 1

min_height, max_height = min(height_dic), max(height_dic)
max_height = min(256, max_height)  # 땅의 높이는 256블록을 초과할 수 없다

result_time = math.inf
result_height = 0

height_dic = sorted(height_dic.items(), reverse=True)

for height in range(min_height, max_height+1):
    time = 0
    block = b

    for key, value in height_dic:
        if key == height:
            continue
        elif key > height:  # 블럭 삭제 2초 소요
            tmp = (key-height) * value
            block += tmp
            time += tmp * 2
        else:  # 블럭 추가 1초 소요
            tmp = (height-key) * value
            block -= tmp
            time += tmp
        if block < 0:  # 블럭 다 씀
            break
    if block < 0:
        continue
    else:
        if time <= result_time:
            result_time = time
            result_height = max(result_height, height)

print(result_time, result_height)



