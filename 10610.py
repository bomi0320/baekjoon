# 30

n = input()
nums = [int(i) for i in n]

if sum(nums) % 3 != 0:  # 3의 배수가 아님
    print(-1)
else:
    nums.sort(reverse=True)
    if nums[-1] != 0:  # 10의 배수가 아님
        print(-1)
    else:  # 30의 배수임!
        for i in nums:
            print(i, end="")
