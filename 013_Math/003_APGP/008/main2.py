#
# 等比数列の和 (2)
#
# https://algo-method.com/tasks/656

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
    N, X, r = map(int, input().split())
    MOD0 = 10**9

    # [ output ]
    """
    S = X * (r^N - 1)/(r-1)
    """
    rN = 1
    for _ in range(N):
        rN *= r
        rN %= MOD0
    s = X * (rN - 1)
    s %= MOD0
    print(s)

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
