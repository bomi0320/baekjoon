# 덩치
import sys

n = int(input())
people = []
for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    h1, w1 = people[i][0], people[i][1]
    rank = 1
    for j in range(n):
        if i == j:
            continue
        else:
            h2, w2 = people[j][0], people[j][1]
            if h1 < h2 and w1 < w2:
                rank += 1
    print(rank, end=" ")


