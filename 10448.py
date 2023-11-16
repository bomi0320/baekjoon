# 유레카 이론
Tri = [] #삼각수
for i in range(1, 46):
    Tri.append(i*(i+1)/2)


def f(num):
    flag = False
    for a in Tri:
        if num <= a:
            break
        for b in Tri:
            if num <= b:
                break
            c = num - (a + b)
            # 성공
            if c in Tri:
                flag = True
                break
        if flag:
            break

    if flag:
        print(1)
    else:
        print(0)


t = int(input())

for _ in range(t):
    k = int(input())
    f(k)
