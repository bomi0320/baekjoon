# 2xn 타일링
def tile(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    tile_list = [0]*(n+1)
    # base case
    tile_list[1] = 1
    tile_list[2] = 2

    for i in range(3, n+1):
        tile_list[i] = tile_list[i-1] + tile_list[i-2]

    return tile_list[n]


n = int(input())
print(tile(n) % 10007)
