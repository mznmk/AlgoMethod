#
# 極限の計算 (1)
#
# https://algo-method.com/tasks/647

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
    A, B = map(int, input().split())

    # [ output ]
    """
    f(x)     = (x^2 + ax + b) / x
             = x + a + b/x        (x != 0)
    lim f(x) = a + lim b/x
    """
    if B == 0:
        print(A)
    elif B < 0:
        print("-inf")
    elif B > 0:
        print("inf")

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
