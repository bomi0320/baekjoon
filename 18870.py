# 좌표 압축

n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(list(set(nums)))
l = len(sorted_nums)

for i in nums:
    left, right = 0, l-1
    while True:
        mid = (left + right) // 2
        if i < sorted_nums[mid]:
            right = mid - 1
        elif i > sorted_nums[mid]:
            left = mid + 1
        else:  # 숫자를 찾음
            print(mid, end=" ")
            break
