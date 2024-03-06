# 배열 합치기

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

nums = a + b
nums.sort()

for num in nums:
    print(num, end=" ")
