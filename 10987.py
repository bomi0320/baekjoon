# 모음의 개수

word = input()

vowels = {"a", "e", "i", "o", "u"}

cnt = 0
for i in word:
    if i in vowels:
        cnt += 1

print(cnt)
