# 수 이어 쓰기 1
N = int(input())

length = len(str(N))

result = 0
for i in range(1, length):
    result += 9 * (10**(i-1)) * i

tmp = '1'+'0'*(length-1)
result += (N-int(tmp)+1) * length

print(result)
