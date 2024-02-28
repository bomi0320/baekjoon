# 숫자 카드

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
to_check = list(map(int, input().split()))

cards.sort()

for check in to_check:
    low, high = 0, n-1
    found = False
    while low <= high:
        mid = (low + high) // 2
        if check > cards[mid]:
            low = mid + 1
        elif check < cards[mid]:
            high = mid - 1
        else:  # 찾음
            found = True
            break
    if found:
        print(1, end=" ")
    else:
        print(0, end=" ")
