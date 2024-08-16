# DNA 비밀번호

from collections import Counter

s, p = map(int, input().split())
DNA = input()
a, c, g, t = map(int, input().split())

result = 0

# 첫번째 부분문자열
counter = Counter(DNA[0:p])
if counter['A'] >= a and counter['C'] >= c and counter['G'] >= g and counter['T'] >= t:
    result += 1

for i in range(1, s-p+1):
    counter[DNA[i-1]] -= 1
    counter[DNA[i+p-1]] += 1
    if counter['A'] >= a and counter['C'] >= c and counter['G'] >= g and counter['T'] >= t:
        result += 1

print(result)
