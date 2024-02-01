# 팰린드롬인지 확인하기

word = input()

flag = True
l = len(word)
for i in range(l//2):
    if word[i] != word[l-i-1]:
        flag = False
        break

if flag:  # 팰린드롬임
    print(1)
else:
    print(0)
