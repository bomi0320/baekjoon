# 접미사 배열
S = input()
result = []
for i in range(len(S)):
    result.append(S[i:])

result.sort()

for r in result:
    print(r)
