# 잃어버린 괄호

input_string = list(input().split("-"))
result = 0


def sum_function(nums):
    n_list = list(map(int, nums.split("+")))
    return sum(n_list)


for i in range(len(input_string)):
    if i == 0:
        result += sum_function(input_string[i])
    else:
        n = sum_function(input_string[i])
        result -= n

print(result)
