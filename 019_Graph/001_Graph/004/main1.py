#
# Q4. 友達の友達
#
# https://algo-method.com/tasks/413

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
    N, M, X = map(int, input().split())

    # [ create graph ]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # [ find friends ]
    fs = set()
    for f in graph[X]:
        fs.add(f)

    # [ find friends of friends ]
    ffs = set()
    for f in graph[X]:
        for ff in graph[f]:
            if ff == X:
                continue
            if ff in fs:
                continue
            ffs.add(ff)

    # [ output ]
    print(len(ffs))

    # # [ for debug ]
    # print(fs)
    # print(ffs)

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
