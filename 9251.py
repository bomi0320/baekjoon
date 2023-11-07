# LCS

def lengthLCS(s, t, m, n):
    length_map = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # base case
    for i in range(m+1):
        length_map[i][0] = 0
    for i in range(n+1):
        length_map[0][i] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                length_map[i][j] = length_map[i-1][j-1] + 1
            else:
                length_map[i][j] = max(length_map[i-1][j], length_map[i][j-1])

    return length_map[m][n]


a = input()
b = input()
m, n = len(a), len(b)
print(lengthLCS(a, b, m, n))
