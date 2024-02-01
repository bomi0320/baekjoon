# 세로읽기
import sys

words = []
max_len = 0
for _ in range(5):
    w = list(sys.stdin.readline().strip())
    words.append(w)
    l = len(w)
    if l > max_len:
        max_len = l

for j in range(max_len):
    for i in range(5):
        try:
            print(words[i][j], end="")
        except IndexError:
            continue
