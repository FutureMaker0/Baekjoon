'''
우선순위 큐

인쇄를 할껀데, 중요도에 따라서 순서를 조정하고자 한다.

1. 현재 queue의 가장 앞에 있는 문서의 중요도를 확인한다.
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
이 문서를 인쇄하지 않고 queue의 가장 뒤에 재배치하고 아니면 바로인쇄

예를 들어, queue에 4개의 문서 a b c d가 있고,
중요도가 2 1 4 3 이라면 인쇄순서는 c d a b 가 된다.

현재 queue에 있는 문서의 수와 중요도가 주어졌을 떄,
어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.

입력
테스트케이스 1
문서의 갯수 N, QUEUE에서 몇 번째 놓여 있는지 나타내는 M
첫 번쨰 index는 0
N개 문서의 중요도가 차례로 주어짐

4 2 - 문서의 갯수는 4개, QUEUE에서 2번째 놓여 있는 현재문서
0 1 2 3 
1 2 3 4 - 4개 문서의 각 중요도

4 2 3 1
3 1 2 - 3은 두 번째로 출력
2 1
1

얘만 가지고 패면...
일단 중요도에 따라 오름차순 정렬
M번째 놓여있는 문서의 가중치 순위를 구해서 몇 번째로 인쇄되는지를
구하면 된다.
인쇄되는 방식에 대한 알고리즘을 제대로 짜는 것이 중요하다
현재 큐의 맨 앞에 인쇄대기중인 것보다 가중치가 높은 애가 뒤에
하나라도 있으면 걔가 맨 앞으로 오고 현재 큐 값은 맨 뒤로 간다
이게 뭘 의미하냐 - popleft한 값을 push 한다는 것.


6 0 - 현재 문서는 첫 번쨰 문서
0 1 2 3 4 5 
1 1 9 1 1 1

9 1 1 1 1 1

'''

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = list(map(int, input().split()))
    q = deque(list(map(int, input().split())))
    # print(q)

    # N개의 숫자에 대한 인덱스 저장 데큐
    index = deque(list(range(N))) 
    
    # c = q[M]
    # print(c) # 3
    # max = max(q)
    # print(max)    

    order = 0
    while q:
        if q[0] == max(q):
            order += 1
            q.popleft()

            pop_index = index.popleft()
            if pop_index == M:
                print(order)
            
        else: # q[0] >= max
            q.append(q.popleft())
            index.append(q.popleft()) 

            
'''
입력
테스트케이스 1
문서의 갯수 N, QUEUE에서 몇 번째 놓여 있는지 나타내는 M
첫 번쨰 index는 0
N개 문서의 중요도가 차례로 주어짐

4 2 - 문서의 갯수는 4개, QUEUE에서 2번째 놓여 있는 현재문서
0 1 2 3 
1 2 3 4 - 4개 문서의 각 중요도

4 2 3 1
3 1 2 - 3은 두 번째로 출력
2 1
1
'''

'''
from collections import deque
import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))
    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            pop_idx = idx.popleft()
            if pop_idx == m:
                print(cnt)
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
'''