# 광고

l = int(input())
s = input()

# pi 구하기
pi = [0 for _ in range(l)]
j = 0
for i in range(1, l):
    while j > 0 and s[i] != s[j]:
        j = pi[j-1]
    if s[i] == s[j]:
        j += 1
        pi[i] = j

print(l - pi[-1])
