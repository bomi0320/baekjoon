# 알파벳 찾기
alpha = [-1] * 26
S = input()

# ord('a') => 97
for i in range(len(S)):
    index = ord(S[i])-97
    if alpha[index] == -1:
        alpha[index] = i

print(*alpha)
