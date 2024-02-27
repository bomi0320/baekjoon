# 5와 6의 차이

a, b = map(str, input().split())

min_a = ''
for i in a:
    if i == '6':
        min_a += '5'
    else:
        min_a += i

min_b = ''
for i in b:
    if i == '6':
        min_b += '5'
    else:
        min_b += i

min_val = int(min_a) + int(min_b)

max_a = ''
for i in a:
    if i == '5':
        max_a += '6'
    else:
        max_a += i

max_b = ''
for i in b:
    if i == '5':
        max_b += '6'
    else:
        max_b += i

max_val = int(max_a) + int(max_b)

print(min_val, max_val)
