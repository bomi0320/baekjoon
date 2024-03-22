# 시리얼 번호

import sys

n = int(input())
serial_number = []
for _ in range(n):
    serial = sys.stdin.readline().strip()
    # serial_number, 길이, 자리수의 합
    serial_number.append([serial, 0, 0])


for i in range(n):
    current = serial_number[i][0]

    # 길이
    serial_number[i][1] = len(current)

    # 자리수의 합
    sum_val = 0
    for j in range(len(current)):
        if current[j].isdigit():
            sum_val += int(current[j])
    serial_number[i][2] = sum_val


serial_number.sort(key=lambda x: (x[1], x[2], x[0]))

# 출력
for current in serial_number:
    print(current[0])
