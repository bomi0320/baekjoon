# 2007년

x, y = map(int, input().split())

tmp = 0
# 월 계산
for i in range(1, x):
    if i == 2:
        tmp += 28
    elif i in [4, 6, 9, 11]:
        tmp += 30
    else:
        tmp += 31

# 일 계산
tmp += y

tmp %= 7
day_dict = {1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU', 5: 'FRI', 6: 'SAT', 0: 'SUN'}

print(day_dict[tmp])
