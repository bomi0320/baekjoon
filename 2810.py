# 컵홀더

n = int(input())
seats = list(input())

cnt = 1
l_cnt = 0
for i in seats:
    if i == 'S':
        cnt += 1
        continue
    else:
        l_cnt += 1
    if l_cnt == 2:
        cnt += 1
        l_cnt = 0

print(min(n, cnt))
