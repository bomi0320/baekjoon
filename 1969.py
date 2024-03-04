# DNA

import sys

n, m = map(int, input().split())
dna = []
for _ in range(n):
    dna.append(sys.stdin.readline().strip())


min_dna = ""
min_hd = 0  # hamming distance의 합
for i in range(m):
    acgt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    for d in dna:
        acgt[d[i]] += 1

    max_tmp = max(acgt, key=acgt.get)
    min_dna += max_tmp

    for key, value in acgt.items():
        if key != max_tmp:
            min_hd += value

# 출력
print(min_dna)
print(min_hd)

