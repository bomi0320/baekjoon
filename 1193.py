# 분수 찾기

X = int(input())

# 위치 찾기
l = 1
while X > l:
    X -= l
    l += 1

if l % 2 == 0:  # 짝
    a, b = X, l-X+1
else:  # 홀
    a, b = l-X+1, X

print(f'{a}/{b}')
