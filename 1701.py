# Cubeditor

s = input()
s_len = len(s)

max_val = 0
for k in range(s_len-1):  # 시작 인덱스: 0, 1, ..., s_len-1
    sub_s = s[k:]
    pi = [0 for _ in range(s_len-k)]

    j = 0
    for i in range(1, s_len-k):
        while (j > 0) and (sub_s[i] != sub_s[j]):
            j = pi[j-1]
        if sub_s[i] == sub_s[j]:
            j += 1
            pi[i] = j

    if max(pi) > max_val:
        max_val = max(pi)

print(max_val)
