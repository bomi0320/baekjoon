# 삼각형과 세 변
while True:
    length = list(map(int, input().split()))

    if not sum(length):  # 0 0 0 입력되면 종료
        break

    length.sort()
    a, b, c = length  # 작은 순으로

    if c >= a + b:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or c == a:
            print("Isosceles")
        else:
            print("Scalene")
