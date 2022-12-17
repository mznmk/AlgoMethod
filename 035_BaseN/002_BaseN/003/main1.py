#
# 2 進法を 16 進法にするプログラム
#
# https://algo-method.com/tasks/1187

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
    S = list(input())
    B = 2

    # [ simulate ]
    # < function >
    def conv2to16(s:list):
        s.reverse()
        v = 0
        p = 1
        for c in s:
            v += p * (ord(c)-ord("0"))
            p *= B
        if v < 10:
            return chr(ord("0") + v)
        else:
            return chr(ord("A") + (v-10))
    # < simulte >
    V = []
    for i in range(0, N, 4):
        V.append(conv2to16(S[i:i+4]))

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
