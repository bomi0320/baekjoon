# 중복 빼고 정렬하기

n = int(input())
nums = list(map(int, input().split()))

num_cnt = {}
for num in nums:
    if num in num_cnt:
        num_cnt[num] += 1
    else:
        num_cnt[num] = 1

num_list = [key for key, value in num_cnt.items()]

num_list.sort()

for num in num_list:
    print(num, end=" ")

