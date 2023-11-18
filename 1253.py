# 좋다

n = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
for c in range(n):
    check = nums[c]
    i = 0
    j = n - 1
    sum = nums[i] + nums[j]
    while i < j:
        if sum == check:
            if i != c and j != c:
                cnt += 1
                break
            elif i == c:
                i += 1
            elif j == c:
                j -= 1
        elif sum > check:
            j -= 1
        else:
            i += 1
        sum = nums[i] + nums[j]

print(cnt)
