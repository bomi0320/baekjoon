# 저울

n = int(input())
weights = list(map(int, input().split()))

weights.sort()

end = 1
for i in range(n):
    now = weights[i]
    if now > end:
        break
    end += now

print(end)

