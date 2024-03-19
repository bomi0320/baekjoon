# 인간-컴퓨터 상호작용

import sys

S = input()
len_S = len(S)

# 누적 합 구하기
arr = [[0 for _ in range(len_S)] for _ in range(26)]
for i in range(26):
    for j in range(len_S):
        if ord(S[j])-97 == i:
            arr[i][j] += 1
        if j > 0:
            arr[i][j] += arr[i][j-1]


q = int(input())
for _ in range(q):
    a, l, r = sys.stdin.readline().split()
    if l == '0':
        print(arr[ord(a) - 97][int(r)])
    else:
        print(arr[ord(a) - 97][int(r)] - arr[ord(a) - 97][int(l)-1])



