# 하얀 칸

import sys

# (i + j)가 0 혹은 2의 배수인 칸에 말이 있는지 확인
cnt = 0
for i in range(8):
    line = list(sys.stdin.readline().rstrip())
    for j in range(8):
        if (i + j) % 2 == 0:
            if line[j] == 'F':
                cnt += 1

print(cnt)
