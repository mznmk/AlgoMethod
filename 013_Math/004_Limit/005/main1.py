#
# 極限の計算 (3)
#
# https://algo-method.com/tasks/667

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
    S = 1 * (r^INF - 1)/(r-1)
    ===
    case: -1 < r < 1
    S = 1/(1-r) => b/(b-a)
    ---
    case: 1 <= r
    S = INF
    """
    if A >= B:
        print(-1)
    else:
        print(f"{B/(B-A):.15f}")

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
