# 나머지 합

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# 합 배열 만들기
sums = []
for i in range(n):
    if i == 0:
        sums.append(nums[0])
    else:
        sums.append(sums[i-1] + nums[i])

l_li = [0]*m
for i in range(n):
    r = sums[i] % m
    l_li[r] += 1

cnt = l_li[0]

for i in range(m):
    if l_li[i] > 1:
        cnt += l_li[i]*(l_li[i]-1)//2

print(cnt)
