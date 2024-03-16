# 예산

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

if sum(nums) <= m:
    print(max(nums))
else:
    start, end = 0, max(nums)
    while start <= end:
        middle = (start + end) // 2

        tmp = 0
        for num in nums:
            tmp += min(middle, num)

        if tmp > m:
            end = middle - 1
        else:
            start = middle + 1
    print(end)

