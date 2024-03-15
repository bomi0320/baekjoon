text = input()
pattern = input()

t_len, p_len = len(text), len(pattern)

# pi 구하기
pi = [0 for _ in range(p_len)]
j = 0
for i in range(1, p_len):
    while (j > 0) and (text[i] != pattern[j]):
        j = pi[j-1]
    if text[i] == pattern[j]:
        j += 1
        pi[i] = j

# kmp
j = 0
for i in range(t_len):
    while (j > 0) and (text[i] != pattern[j]):
        j = pi[j-1]
    if text[i] == pattern[j]:
        if j == p_len - 1:  # 찾음
            print(i)
            j = pi[j]
        else:
            j += 1
