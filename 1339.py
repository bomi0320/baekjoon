# 단어 수학

n = int(input())
words = []
for _ in range(n):
    words.append(input())

position = dict()
for word in words:
    for i in range(len(word)):
        w = word[i]
        if w in position:
            position[w] += 10**(len(word) - i)
        else:
            position[w] = 10**(len(word) - i)

position = sorted(position.items(), key=lambda x: x[1], reverse=True)
# print(position)

alpha = dict()
num = 9
for i in position:
    alpha[i[0]] = num
    num -= 1
# print(alpha)

result = 0
for word in words:
    now = ''
    for w in word:
        now += str(alpha[w])
    result += int(now)

print(result)