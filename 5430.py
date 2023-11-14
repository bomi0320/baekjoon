# AC
from collections import deque
import sys


def f(orders, n_queue):
    cnt_r = 0
    for o in orders:
        if o == 'R':
            cnt_r += 1

        else:  # D
            if len(n_queue) == 0:
                print("error")
                return

            if cnt_r % 2 == 0:
                n_queue.popleft()
            else:
                n_queue.pop()

    if len(n_queue) == 0:
        print("[]")
        return

    if cnt_r % 2 != 0:
        n_queue.reverse()

    # 출력
    print("[", end="")
    length = len(n_queue)
    for i in range(length):
        if i != (length-1):
            print(str(n_queue.popleft()) + ",", end="")
        else:
            print(str(n_queue.popleft()), end="")
    print("]", end="\n")


t = int(sys.stdin.readline())
for _ in range(t):
    order = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    if n == 0:
        li = sys.stdin.readline()
        queue = deque([])
        f(order, queue)
    else:
        nums = list(map(int, sys.stdin.readline()[1:-2].split(",")))
        queue = deque(nums)

        f(order, queue)
