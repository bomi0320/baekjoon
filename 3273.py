# 두 수의 합

n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()  # 오름차순 정렬

cnt = 0
left, right = 0, n-1  # left, right는 인덱스 값. left는 왼->오로 이동, right는 왼<-오로 이동
while left < right:  # left, right 값이 같아지면 종료
    sum_val = nums[left] + nums[right]
    if sum_val == x:  # 합이 x라면
        cnt += 1  # 카운트 증가
        left += 1
        right -= 1
    elif sum_val > x:
        right -= 1
    else:  # sum_val < x
        left += 1

print(cnt)
