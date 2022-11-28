#
# 面積を求める (3)
#
# https://algo-method.com/tasks/604

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
    A, B, H = map(int, input().split())

    # [ simulate ]
    # < function >
    def f(x):
        return (B-A)/H * x + A
    # < simulate >
    for k in range(0, 5+1):
        # find square
        S = 0
        n = 10**k
        for i in range(n):
            S += f((H/n)*i) * H/n
        # print square
        print(f"{S:.15f}")

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
