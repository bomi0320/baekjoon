# 진법 변환

N, B = input().split()
N = N[::-1]  # 순서 반대로 저장
B = int(B)

result = 0
for i in range(len(N)):
    n = 0
    if N[i].isdigit():  # N[i]이 숫자(0~9)일때
        n = int(N[i])
    else:  # N[i]이 알파벳 대문자일 때
        # ord(A) => 65이기 때문에 55를 빼준다
        n = ord(N[i]) - 55
    result += n * (B**i)

print(result)
