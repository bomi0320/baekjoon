# DNA 비밀번호

s, p = map(int, input().split())
dna_string = input()
a, c, g, t = map(int, input().split())

cnt = 0
# 최초의 window
start = dna_string[0:p]
# 처음 상태 체크
state = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for w in start:
    state[w] += 1
if state['A'] >= a and state['C'] >= c and state['G'] >= g and state['T'] >= t:
    cnt += 1

for i in range(1, s-p+1):
    # i-1번째 상태 빼기
    state[dna_string[i-1]] -= 1
    # i+p번째 상태 더하기
    state[dna_string[i+p-1]] += 1
    if state['A'] >= a and state['C'] >= c and state['G'] >= g and state['T'] >= t:
        cnt += 1

print(cnt)
