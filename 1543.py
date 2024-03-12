# 문서 검색

s = input()
word = input()

l = len(s)
w_len = len(word)

start = 0
result = 0

while start < l:
    index = s.find(word, start)
    if index >= 0:
        result += 1
        start = index + w_len
    else:
        break

print(result)


