# 암호 만들기
from itertools import combinations

l, c = map(int, input().split())
alpha = list(input().split())

alpha.sort()


def num_of_vowel(letter):
    count = 0
    for i in range(len(letter)):
        if letter[i] in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


combs = combinations(alpha, l)
for c in combs:
    vow = num_of_vowel(c)  # 모음의 개수
    con = l - vow  # 자음의 개수
    if vow >= 1 and con >= 2:
        print("".join(c))
