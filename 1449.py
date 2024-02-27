# 수리공 항승

n, l = map(int, input().split())
points = list(map(int, input().split()))

points.sort(reverse=True)

p = points.pop()
start = p - 0.5
end = start + l
cnt = 1
while points:
    p = points.pop()
    if p < end:
        continue
    else:
        start = p - 0.5
        end = start + l
        cnt += 1
print(cnt)
