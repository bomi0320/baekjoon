# DNA 비밀번호

S, P = map(int, input().split())
DNA = input()
ACGT = list(map(int, input().split()))

check_num = 0
for i in range(4):
    if ACGT[i] == 0:
        check_num += 1


def increase(c):
    global check_num
    if c == 'A':
        counter['A'] += 1
        if counter['A'] == ACGT[0]:
            check_num += 1
    elif c == 'C':
        counter['C'] += 1
        if counter['C'] == ACGT[1]:
            check_num += 1
    elif c == 'G':
        counter['G'] += 1
        if counter['G'] == ACGT[2]:
            check_num += 1
    else:  # 'T'
        counter['T'] += 1
        if counter['T'] == ACGT[3]:
            check_num += 1


def decrease(c):
    global check_num
    if c == 'A':
        if counter['A'] == ACGT[0]:
            check_num -= 1
        counter['A'] -= 1
    elif c == 'C':
        if counter['C'] == ACGT[1]:
            check_num -= 1
        counter['C'] -= 1
    elif c == 'G':
        if counter['G'] == ACGT[2]:
            check_num -= 1
        counter['G'] -= 1
    else:  # 'T'
        if counter['T'] == ACGT[3]:
            check_num -= 1
        counter['T'] -= 1


# 초기 설정
counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(P):
    increase(DNA[i])

result = 0
if check_num == 4:
    result += 1

for i in range(S-P):
    decrease(DNA[i])
    increase(DNA[i+P])
    if check_num == 4:
        result += 1

print(result)
