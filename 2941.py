# 크로아티아 알파벳

word = input()
croatia_2 = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]  # 2글자로 된 크로아티아 문자

l = len(word)
result = 0

if l == 0:
    print(0)
elif l == 1:  # 알파벳임
    if word.isalpha():
        print(1)
    else:
        print(0)
else:
    start = 0
    while start < l:
        if (start+2 <= l) and (word[start:start+2] in croatia_2):  # 2글자가 croatia 리스트에 있는지 확인
            result += 1
            start += 2
        elif (start + 3 <= l) and (word[start:start+3] == "dz="):  # 문자에 dz=(유일한 3글자)가 있는지 확인
            result += 1
            start += 3
        else:  # 알파벳임
            if word[start].isalpha():
                result += 1
            start += 1
    print(result)
