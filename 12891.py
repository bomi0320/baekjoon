# DNA 비밀번호

# input
S, P = map(int, input().split())
DNA = input()
ACGT = list(map(int, input().split()))


# 함수
def add(c):
    global num_of_clear
    if c == 'A':
        num_of_acgt[0] += 1
        if num_of_acgt[0] == ACGT[0]:
            num_of_clear += 1
    elif c == 'C':
        num_of_acgt[1] += 1
        if num_of_acgt[1] == ACGT[1]:
            num_of_clear += 1
    elif c == 'G':
        num_of_acgt[2] += 1
        if num_of_acgt[2] == ACGT[2]:
            num_of_clear += 1
    else:  # 'T'
        num_of_acgt[3] += 1
        if num_of_acgt[3] == ACGT[3]:
            num_of_clear += 1


def subtract(c):
    global num_of_clear
    if c == 'A':
        if num_of_acgt[0] == ACGT[0]:
            num_of_clear -= 1
        num_of_acgt[0] -= 1
    elif c == 'C':
        if num_of_acgt[1] == ACGT[1]:
            num_of_clear -= 1
        num_of_acgt[1] -= 1
    elif c == 'G':
        if num_of_acgt[2] == ACGT[2]:
            num_of_clear -= 1
        num_of_acgt[2] -= 1
    else:
        if num_of_acgt[3] == ACGT[3]:
            num_of_clear -= 1
        num_of_acgt[3] -= 1


# 초기 설정
num_of_acgt = [0, 0, 0, 0]
num_of_clear = 0
result = 0

for acgt in ACGT:
    if acgt == 0:
        num_of_clear += 1


# 첫번째 DNA 부분문자열
for i in range(P):
    add(DNA[i])

if num_of_clear == 4:
    result += 1

# DNA 부분문자열
for i in range(1, S-P+1):
    subtract(DNA[i-1])
    add(DNA[i+P-1])
    if num_of_clear == 4:
        result += 1

print(result)
