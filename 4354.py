# 문자열 제곱

import sys

while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break

    l = len(s)

    # pi
    pi = [0 for _ in range(l)]
    j = 0
    for i in range(1, l):
        while (j > 0) and (s[i] != s[j]):
            j = pi[j-1]
        if s[i] == s[j]:
            j += 1
            pi[i] = j

    p_len = l - pi[-1]
    if l % p_len == 0:
        print(l // p_len)
    else:
        print(1)
