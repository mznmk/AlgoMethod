#
# Q3. 人気者の友達
#
# https://algo-method.com/tasks/673

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
    N, M = map(int, input().split())

    # [ create graph ]
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # [ find student ]
    max_f = 0
    max_i = -1
    for i in range(N):
        if max_f < len(graph[i]):
            max_f = len(graph[i])
            max_i = i

    # [ output ]
    graph[max_i].sort()
    print(*graph[max_i])

    # # [ for debug ]
    # print(graph)
    # print(max_f)
    # print(max_i)

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
