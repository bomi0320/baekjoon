# 알파벳 개수
alpha = [0] * 26
S = input()

# ord('a') => 97
for s in S:
    alpha[ord(s)-97] += 1

print(*alpha)
