# 문자열 폭발

s = list(input())
explosion = input()

l = len(s)  # 문자열의 길이
explo_l = len(explosion)  # 폭발 문자열의 길이
explo_last = explosion[-1]  # 폭발 문자열의 마지막 문자

stack = []  # 스택
j = 0  # 폭발 문자열의 인덱스
flag = False
for i in range(l):
    if s[i] == explo_last:  # 폭발 문자열의 마지막 문자와 같으면
        flag = True
        tmp_list = [explo_last]
        for j in range(explo_l-2, -1, -1):
            if not stack:  # 폭발 문자열이 아님
                flag = False
                break
            else:
                tmp = stack.pop()
                tmp_list.append(tmp)
                if tmp != explosion[j]:  # 폭발 문자열이 아님
                    flag = False
                    break

        if not flag:  # 폭발 문자열이 아니였으면
            stack.extend(tmp_list[::-1])  # pop 한 문자열들 전부 다시 push

    else:
        stack.append(s[i])


if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))
