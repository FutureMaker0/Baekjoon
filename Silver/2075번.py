'''
우선순위 큐

N번째 큰 수 찾기 프로그램
단, 표에 채워진 수는 모두 다르다.
'''

'''
import sys
from collections import deque

N = int(input())

for i in range(N):
    q = deque(list(map(int, input().split())))
    
    q = sorted(q)
    # print(max(q2))
    max_val = max(q)
    print(max_val)
'''

'''
문제 설명에서 아래 숫자는 무조건 위에 애보다 크다라는게 힌트인 듯.
아마 여기서 heapq를 쓰라는 걸 알려주는 것 같다.

최소 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 작은 힙
최대 힙: 부모 노드의 키값이 자식 노드의 키값보다 항상 큰 힙

파이썬에서의 힙은 최소힙을 기반으로 하기에 사용이 가능하다.

'''

import heapq

N = int(input())

heap = []
for _ in range(N):
    nums = map(int, input().split())
    for num in nums:
        if len(heap) < N: # N = 5
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])

'''
1 2 3 4
2 3 4
2 3 4 5
3 4 5
3 4 5 6
4 5 6
4 5 6 7
5 6 7
5 6 7 8
6 7 8
6 7 8 9
7 8 9 -> 7을 출력

'''



