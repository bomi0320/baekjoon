# 단어 뒤집기 2

strng = list(input())
temp = []

flag = False  # <>안에 있는지 확인

for chr in strng:
    if chr == ' ':
        if flag:
            temp.append(" ")
        # temp에 들어있는 것 뒤집어서 출력
        if not flag and len(temp) != 0:
            print("".join(temp[::-1]), end=" ")
            temp = []
    elif chr == '<':
        flag = True
        # temp에 들어있는 것 뒤집어서 출력
        if len(temp) != 0:
            print("".join(temp[::-1]), end="")
            temp = []
    elif chr == '>':
        flag = False
        # temp에 들어있는 것 그대로 출력
        print("<" + "".join(temp) + ">", end="")
        temp = []
    else:
        temp.append(chr)

if len(temp) != 0:
    print("".join(temp[::-1]), end=" ")