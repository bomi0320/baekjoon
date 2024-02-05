# 문자열 분석

while True:
    try:
        S = input()
        result = [0] * 4  # 소문자, 대문자, 숫자, 공백

        for s in S:
            if s.islower():   # 소문자
                result[0] += 1
            elif s.isupper():  # 대문자
                result[1] += 1
            elif s.isdigit():  # 숫자
                result[2] += 1
            else:  # 공백
                result[3] += 1

        print(*result)

    except EOFError:
        break
