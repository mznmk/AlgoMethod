#
# 直線の傾き (2)
#
# https://algo-method.com/tasks/581

# ---------------------------------------------------------------------------- #

from time import process_time
import sys
sys.setrecursionlimit(10**9)

MOD9 = 10**9+9
MOD7 = 10**9+7
MOD3 = 998244353

# ---------------------------------------------------------------------------- #

def solve():
    # [ input ]
    N, A, B = map(int, input().split())

    # [ simulate ]
    """
    slope = (B^2-A^2)/(B-A)
          = (B-A)(B+A)/(B-A)
          = B+A
    """
    for _ in range(N):
        # find slope
        print(f"{A+B:.10f}")
        # move next
        B = (A+B)/2

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
