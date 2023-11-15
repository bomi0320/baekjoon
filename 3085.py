# 사탕 게임
import sys


# 사탕의 최대 개수 계산
def compute_max_val(n, board):
    max_val = 0
    # 가로로 최대 개수 계산
    max_tmp = 1
    for i in range(n):
        max_tmp = 1
        for j in range(1, n):
            if board[i][j-1] == board[i][j]:
                max_tmp += 1
            else:
                if max_tmp > max_val:
                    max_val = max_tmp
                max_tmp = 1
        if max_tmp > max_val:
            max_val = max_tmp
    if max_tmp > max_val:
        max_val = max_tmp


    # 세로로 최대 개수 계산
    max_tmp = 1
    for j in range(n):
        max_tmp = 1
        for i in range(1, n):
            if board[i-1][j] == board[i][j]:
                max_tmp += 1
            else:
                if max_tmp > max_val:
                    max_val = max_tmp
                max_tmp = 1
        if max_tmp > max_val:
            max_val = max_tmp
    if max_tmp > max_val:
        max_val = max_tmp

    return max_val


def change(n, board):
    r_max, c_max = 0, 0
    # 가로로 인접한 두 칸 교환
    for i in range(n):
        for j in range(1, n):
            if board[i][j-1] != board[i][j]:  # 다르면 swap
                board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
                # 사탕의 최대 개수 계산
                r_tmp = compute_max_val(n, board)
                if r_tmp > r_max:
                    r_max = r_tmp
                # 원래대로 돌려놓기
                board[i][j - 1], board[i][j] = board[i][j], board[i][j - 1]

    # 세로로 인접한 두 칸 교환
    for j in range(n):
        for i in range(1, n):
            if board[i-1][j] != board[i][j]:  # 다르면 swap
                board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
                # 사탕의 최대 개수 계산
                c_tmp = compute_max_val(n, board)
                if c_tmp > c_max:
                    c_max = c_tmp
                # 원래대로 돌려놓기
                board[i-1][j], board[i][j] = board[i][j], board[i-1][j]

    return max(r_max, c_max)


n = int(input())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

print(change(n, board))
#print(compute_max_val(n, board))
