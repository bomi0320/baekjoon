# 스네이크버드

n, l = map(int, input().split())
h_list = list(map(int, input().split()))

h_list.sort()

for h in h_list:
    if l < h:
        break
    else:
        l += 1

print(l)
