# 농구 경기

import sys

n = int(input())

players_dict = {}
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    first_name = name[0]

    if first_name in players_dict:
        players_dict[first_name] += 1
    else:
        players_dict[first_name] = 1


#  성의 첫 글자가 같은 선수가 5명보다 경우, 성의 첫 글자를 tmp에 저장
tmp = []
for first_name, cnt in players_dict.items():
    if cnt >= 5:
        tmp.append(first_name)


if len(tmp) == 0:  # 다섯 명을 선발할 수 없는 경우
    print("PREDAJA")
else:
    tmp.sort()  # 사전 순으로 정렬
    print("".join(tmp))
