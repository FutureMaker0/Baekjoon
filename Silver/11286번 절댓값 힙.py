# 1 -1 0 0 0 1 1 -1 -1 2 -2 0 0 0 0 0 0 0

# heap
# -1 1 0 -1 -1 1 1 -2 2 0

import sys
import heapq

N = int(input())

heap = []
for _ in range(N):
    # x = map(int, input().split())
    x = int(sys.stdin.readline())

    if x == 0:
        if not heap:
            print(0)
        else:
            # print(min(abs(x)))
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))
