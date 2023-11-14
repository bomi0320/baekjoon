# 체스판 다시 칠하기
import sys


def chessboard(board, x_start, x_end, y_start, y_end):
    color = ['W', 'B']

    # WBWBWBWB~~
    start1 = -1  # start 'W'
    start2 = 0  # start 'B'
    temp1 = 0
    temp2 = 0
    for x in range(x_start, x_end+1):
        for y in range(y_start, y_end+1):
            start1 += 1
            if board[x][y] != color[start1 % 2]:
                temp1 += 1

            start2 += 1
            if board[x][y] != color[start2 % 2]:
                temp2 += 1
        start1 -= 1
        start2 -= 1

    return min(temp1, temp2)


n, m = map(int, input().split())
board = []
for _ in range(n):
    one_line = list(sys.stdin.readline().strip())
    board.append(one_line)

if n > 8 or m > 8:  # 체스판 잘라야 함
    min_val = 64
    cnt = 0
    for i in range(n-7):
        for j in range(m-7):
            result = chessboard(board, i, i+7, j, j+7)
            if result <= min_val:
                min_val = result
    print(min_val)
else:
    print(chessboard(board, 0, 7, 0, 7))
