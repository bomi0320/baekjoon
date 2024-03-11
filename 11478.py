# 서로 다른 부분 문자열의 개수

s = input()

l = len(s)
substring = set()
for i in range(1, l+1):
    for j in range(0, l-i+1):
        substring.add(s[j:j+i])

print(len(substring))
