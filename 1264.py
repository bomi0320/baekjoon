# 모음의 개수
import sys

vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

while True:
    line = sys.stdin.readline().rstrip()
    if line == "#":  # 종료
        break

    cnt = 0
    for i in line:
        if i in vowel:
            cnt += 1

    print(cnt)
