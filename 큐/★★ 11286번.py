'''
절댓값 힙

절댓값 힙은 아래와 같은 연산을 지원하는 자료구조

1. 배열에 정수 x를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거
   절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고
   그 값을 배열에서 제거한다.

프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

'''
import heapq

N = int(input())

heap = []
for _ in range(N):
    xs = map(int, input().split())

    for x in xs:
        if x == 0:
            if not heap:
                print(0)
            else:
                # print(min(abs(x)))
                heapq.heappop(heap)
        else:
            heapq.heappush(heap, x)
            # print(heap)
'''

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

