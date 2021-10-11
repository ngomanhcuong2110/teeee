import os
import sys

#
# Complete the rustMurdered function below.
#
def rustMurderer(n, roads, s):
    ed = [[] for _ in range(n)]
    for u, v in roads:
        ed[u-1].append(v-1)
        ed[v-1].append(u-1)
    d = [-1] * n
    prev = [s-1]
    d[s-1] = 0
    cur = 0
    while prev:
        cur += 1
        cnt = [0] * n
        for u in prev:
            for v in ed[u]:
                if d[v] == -1:
                    cnt[v] += 1
        nxt = []
        for u in range(n):
            if d[u] == -1 and cnt[u] < len(prev):
                d[u] = cur
                nxt.append(u)
        prev = nxt
    return d[:s-1] + d[s:]

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        roads = []

        for _ in range(m):
            roads.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = rustMurderer(n, roads, s)
        print(result)