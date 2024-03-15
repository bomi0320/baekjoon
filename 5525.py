# IOIOI

n = int(input())
m = int(input())
s = input()

p = "I" + "OI" * n
p_len = len(p)

# pi 구하기
pi = [i for i in range(-1, p_len-1)]
pi[0] = 0

# kmp
result = 0
j = 0
for i in range(m):
    while (j > 0) and (s[i] != p[j]):
        j = pi[j-1]
    if s[i] == p[j]:
        if j == p_len - 1:
            result += 1
            j = pi[j]
        else:
            j += 1

print(result)
