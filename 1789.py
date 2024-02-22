# 수들의 합

s = int(input())

i = 1
while True:
    if i * (i+1) / 2 > s:
        break
    i += 1

print(i-1)
