# 베스트셀러

import sys

n = int(input())
books = {}
for _ in range(n):
    book = sys.stdin.readline().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max_val = max(books.values())

tmp = []
for key, value in books.items():
    if value == max_val:
        tmp.append(key)

tmp.sort()

print(tmp[0])
