# 삼각형 외우기

a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
else:
    if a == 60 and b == 60:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
