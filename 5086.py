# 배수와 약수

while True:
    a, b = map(int, input().split())

    if a == 0:
        break

    if a < b:
        # case 1
        if b % a == 0:
            print("factor")
        else:
            print("neither")
    else:
        if a % b == 0:
            print("multiple")
        else:
            print("neither")
