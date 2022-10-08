#
# for文とシグマ計算 (1)
#
# https://algo-method.com/tasks/566

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

    # [ simulate ]
    sumN = 0
    for v in range(1, N+1):
        sumN += v

    # [ output ]
    print(sumN)

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
