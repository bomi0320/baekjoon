# 열 개씩 끊어 출력하기

s = input()

l = len(s)
start = 0
end = min(l, start+10)

while start < end:
    print(s[start:end])
    start = end
    end = min(l, start+10)
