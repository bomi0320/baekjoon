# 팰린드롬 만들기

data = list(input())
n = len(data)

alpha_dict = {}
for d in data:
    if d in alpha_dict:
        alpha_dict[d] += 1
    else:
        alpha_dict[d] = 1

# 홀수개인 알파벳 개수 세기
num_of_odd = 0
odd_alpha = ''
for key, value in alpha_dict.items():
    if value % 2 != 0:
        num_of_odd += 1
        odd_alpha += key

alpha_dict = sorted(alpha_dict.items())  # 알파벳 순으로 정렬

if n % 2 == 0:  # 문자열 길이가 짝수일 때
    if num_of_odd > 0:
        print("I'm Sorry Hansoo")
    else:
        result = ''
        for key, value in alpha_dict:
            result += key * (value // 2)
        tmp = result[:n // 2][::-1]
        result += tmp
        print(result)

else:  # 문자열 길이가 홀수일 때
    if num_of_odd > 1:
        print("I'm Sorry Hansoo")
    else:
        result = ''
        for key, value in alpha_dict:
            result += key * (value//2)
        result += odd_alpha
        tmp = result[:n//2][::-1]
        result += tmp
        print(result)
