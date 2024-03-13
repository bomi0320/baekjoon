# 찾기

t = input()
p = input()

t_len, p_len = len(t), len(p)

# pi 구하기
pi = [0 for _ in range(p_len)]
j = 0
for i in range(1, p_len):
    while j > 0 and p[i] != p[j]:
        j = pi[j-1]
    if p[i] == p[j]:
        j += 1
        pi[i] = j

# kmp
cnt = 0
result = []

j = 0  # p의 index
for i in range(t_len):
    while j > 0 and t[i] != p[j]:
        j = pi[j-1]

    if t[i] == p[j]:
        if j == p_len - 1:  # 패턴을 찾음
            cnt += 1
            result.append(str(i-p_len+2))
            j = pi[j]
        else:
            j += 1

print(cnt)
print(" ".join(result))
