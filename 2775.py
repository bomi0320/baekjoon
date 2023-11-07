# 부녀회장이 될테야

def apa(k, n):
    apartment = [[0 for j in range(n + 1)] for i in range(k + 1)]

    # base case
    for i in range(n + 1):
        apartment[0][i] = i

    for i in range(1, k + 1):
        for j in range(1, n + 1):
            for l in range(1, j + 1):
                apartment[i][j] += apartment[i - 1][l]

    return apartment[k][n]


t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(apa(k, n))
