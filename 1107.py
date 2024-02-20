# 리모컨

N = int(input())
M = int(input())
if M != 0:
    broken_button = input().split()
else:
    broken_button = []

result = abs(100-N)

for i in range(1000000):
    num = str(i)
    for n in num:
        if n in broken_button:
            break
    else:
        result = min(result, len(num) + abs(i-N))

print(result)
