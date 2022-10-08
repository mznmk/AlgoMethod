#
# 標準入力 3-10
#
# https://algo-method.com/tasks/62

# ---------------------------------------------------------------------------- #

from time import process_time
import sys
sys.setrecursionlimit((10**5)*5)

MOD9 = 10**9+9
MOD7 = 10**9+7
MOD3 = 998244353

# ---------------------------------------------------------------------------- #

def solve():
    # [ input ]
    N = int(input())
    S = [input() for _ in range(N)]

    # [ simulate ]
    lr = dict()
    for s in S:
        if s in lr:
            lr[s] += 1
        else:
            lr[s] = 1

    # [ output ]
    lc = lr["left"]
    rc = lr["right"]
    if (lc == rc):
        print("same")
    elif (lc < rc):
        print("right")
    else:
        print("left")

    # [ return ]
    return

# ---------------------------------------------------------------------------- #

if __name__ == '__main__':
    if __debug__:
        # [ submit ]
        solve()
    else:
        # [ test samples ]
        # set I/O
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')
        # test samples
        times = int(input())
        for i in range(1, times+1):
            input()
            print(f'[ sample: {i} ]')
            start = process_time()
            solve()
            end = process_time()
            print(f'(Run Time: {(end-start)*1000:f} ms)\n')
