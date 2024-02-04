# 단어 뒤집기
t = int(input())
for _ in range(t):
    sentence = input().split()
    for s in sentence:
        print(s[::-1], end=" ")
    print()
