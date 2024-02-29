# 나무 자르기

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

last_total = 0
while start <= end:
    middle = (start + end) // 2
    total = 0
    for tree in trees:
        tmp = tree - middle
        if tmp > 0:
            total += tmp
    if total >= m:
        start = middle + 1
    else:
        end = middle - 1

print(end)
