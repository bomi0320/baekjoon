# A와 B

s = input()
t = input()

n = len(s)

while len(t) != n:
    if t[-1] == 'A':
        t = t[:-1]
    else:  # 'B'
        t = t[:-1][::-1]

if s == t:
    print(1)
else:
    print(0)
