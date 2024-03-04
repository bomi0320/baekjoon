# 사과 담기 게임

import sys

m, n = map(int, input().split())  # n: 현재 위치
start, end = 1, n

j = int(input())  # 떨어지는 사과의 개수

result = 0
for _ in range(j):
    position = int(sys.stdin.readline())

    if start <= position <= end:
        continue

    elif position < start:
        tmp = start - position
        result += tmp
        # start, end 위치 조정하기
        start -= tmp
        end -= tmp

    else:  # position > end
        tmp = position - end
        result += tmp
        # start, end 위치 조정하기
        end += tmp
        start += tmp

print(result)
