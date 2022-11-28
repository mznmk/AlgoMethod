#
# 円周率を求める
#
# https://algo-method.com/tasks/606

# ---------------------------------------------------------------------------- #

from time import process_time
import sys
sys.setrecursionlimit(10**9)

from math import sqrt

MOD9 = 10**9+9
MOD7 = 10**9+7
MOD3 = 998244353

# ---------------------------------------------------------------------------- #

def solve():
    # [ input ]
    N = int(input())

    # [ simulate ]
    # < function >
    def f(x):
        return sqrt(1-x*x)
    # < simulate >
    S = 0
    for k in range(N):
        S += f((1/N)*k) * 1/N
    S *= 4

    # [ output ]
    print(f"{S:.10f}")

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
