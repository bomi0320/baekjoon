# DNA 비밀번호

S, P = map(int, input().split())
DNA = list(input().strip())
ACGT = list(map(int, input().split()))

this_acgt = [0, 0, 0, 0]  # A, C, G, T
clear = 0
count = 0

for acgt in ACGT:
    if acgt == 0:
        clear += 1


def add(c):
    global clear
    if c == 'A':
        this_acgt[0] += 1
        if this_acgt[0] == ACGT[0]:
            clear += 1
    elif c == 'C':
        this_acgt[1] += 1
        if this_acgt[1] == ACGT[1]:
            clear += 1
    elif c == 'G':
        this_acgt[2] += 1
        if this_acgt[2] == ACGT[2]:
            clear += 1
    else:  # 'T
        this_acgt[3] += 1
        if this_acgt[3] == ACGT[3]:
            clear += 1


def subtract(c):
    global clear
    if c == 'A':
        if this_acgt[0] == ACGT[0]:
            clear -= 1
        this_acgt[0] -= 1
    elif c == 'C':
        if this_acgt[1] == ACGT[1]:
            clear -= 1
        this_acgt[1] -= 1
    elif c == 'G':
        if this_acgt[2] == ACGT[2]:
            clear -= 1
        this_acgt[2] -= 1
    else:  # 'T
        if this_acgt[3] == ACGT[3]:
            clear -= 1
        this_acgt[3] -= 1


for i in range(P):
    add(DNA[i])
if clear == 4:
    count += 1

for i in range(P, S):
    subtract(DNA[i-P])
    add(DNA[i])
    if clear == 4:
        count += 1

print(count)
