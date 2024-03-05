# 나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int, input().split())
pokemon = {}
for i in range(1, n+1):  # n: 도감에 수록되어 있는 포켓몬의 개수
    name = sys.stdin.readline().rstrip()
    pokemon[str(i)] = name
    pokemon[name] = str(i)

for _ in range(m):  # m: 맞춰야 하는 문제의 개수
    q = str(sys.stdin.readline().rstrip())
    print(pokemon[q])
