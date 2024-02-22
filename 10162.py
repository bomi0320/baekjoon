# 전자레인지

t = int(input())
times = [300, 60, 10]
cnt = [0, 0, 0]

for i in range(3):
    time = times[i]
    if times[i] > t:
        continue
    while times[i] <= t:
        t -= time
        cnt[i] += 1

if t > 0:
    print(-1)
else:
    for i in range(3):
        print(cnt[i], end=" ")
