# 그릇

bowls = input()

last = bowls[0]
l = len(bowls)
result = 10

for i in range(1, l):
    if last == bowls[i]:
        result += 5
    else:
        result += 10
    last = bowls[i]

print(result)
