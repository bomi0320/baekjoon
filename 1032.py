# 명령 프롬프트

import sys

n = int(input())

result = list(input())
l = len(result)

for _ in range(n-1):
    s = sys.stdin.readline().strip()
    for i in range(l):
        if s[i] != result[i]:
            result[i] = "?"

print("".join(result))
