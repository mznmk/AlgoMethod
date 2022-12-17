#
# 10 進法を N 進法にするプログラム
#
# https://algo-method.com/tasks/1186

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
    N = int(input())
    S = int(input())

    # [ simulate ]
    V = []
    while S:
        d = S % N
        c = chr(ord("0") + d)
        V.append(c)
        S //= N
    V.reverse()
    if not V:
        V.append("0")

    # [ output ]
    print("".join(V))

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
