# 그대로 출력하기 2

while True:
    try:
        line = input()
        print(line)
    except EOFError:
        break
