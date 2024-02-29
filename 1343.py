# 폴리오미노

board = input().split(".")

result = []
flag = True
for i in board:
    l = len(i)
    if l % 2 != 0:  # 덮을 수 없음
        flag = False
        break
    else:
        if l % 4 == 0:
            result.append("A" * l)
        elif l > 2:
            result.append('A'*(l-2) + 'BB')

        else:  # l == 2
            result.append('BB')


if not flag:
    print("-1")
else:
    answer = ''
    for i in result:
        if not i:
            answer += "."
            continue
        else:
            answer += i
        answer += "."

    print(answer[:-1])
