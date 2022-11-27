#
# どこまでも続く数列 (2)
#
# https://algo-method.com/tasks/663

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
         r <= -1 --> type 3
    -1 < r <= 1  --> type 1
     1 < r       --> type 2
    ---
    r = A/B
    """
    if A <= -B:
        print(3)
    elif -B < A <= B:
        print(1)
    elif B < A:
        print(2)

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
