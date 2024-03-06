# 베시와 데이지

b1, b2 = map(int, input().split())
d1, d2 = map(int, input().split())
j1, j2 = map(int, input().split())

bessie_gap = max(abs(j1-b1), abs(j2-b2))
daisy_gap = abs(j1-d1) + abs(j2-d2)

if bessie_gap < daisy_gap:
    print("bessie")
elif bessie_gap > daisy_gap:
    print("daisy")
else:
    print("tie")
