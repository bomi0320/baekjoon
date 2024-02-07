# -2진수

n = int(input())

# print(1//-2, 1%-2)  # -1 -1
# print(2//-2, 2%-2)  # -1 0
# print(-1//-2, -1%-2)  # 0 -1
# print(-13//-2, -13%-2)  # 6 -1

if n == 0:
    print(0)
else:
    result = ""
    while n:
        if n % -2 == 0:
            result += "0"
            n //= -2
        else:  # 나머지가 1일 때
            result += "1"
            n = n // -2 + 1

    print(result[::-1])
