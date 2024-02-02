# 약수들의 합

while True:
    n = int(input())

    if n == -1:  # 종료
        break

    # 약수 구하기
    aliquot = []
    for i in range(1, n):
        if n % i == 0:
            aliquot.append(i)

    # 완전수인지 확인
    if sum(aliquot) == n:  # 완전수
        print(n, "=", " + ".join(map(str, aliquot)))
    else:
        print(f"{n} is NOT perfect.")
