# 가장 긴 증가하는 부분 수열 2

n = int(input())
nums = list(map(int, input().split()))

tmp = [0]
for num in nums:
    if tmp[-1] < num:
        tmp.append(num)
    else:
        left = 0
        right = len(tmp)
        while left < right:
            mid = (left + right) // 2
            if tmp[mid] < num:
                left = mid + 1
            else:
                right = mid
        tmp[right] = num

print(len(tmp) - 1)
