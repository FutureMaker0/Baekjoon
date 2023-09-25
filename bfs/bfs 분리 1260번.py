'''
1260 번

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 
작성하시오. 단, 방문할 수 있는 "정점이 여러 개인 경우에는 정점 번호가 
작은 것을 먼저 방문"하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
"정점 번호는 1번부터 N번까지"이다.

bfs만 분리.

예제 입력,
5 5 3 - 5개의 노드, 5개의 간선, 시작노드 3
5 4 - 5번 노드에 4번 노드 연결 
5 2 - 5번 노드에 2번 노드 연결
1 2 - 1번 노드에 2번 노드 연결
3 4 - 3번 노드에 4번 노드 연결
3 1 - 3번 노드에 1번 노드 연결

예제 출력:
3 1 4 2 5 - 순서대로 탐색

'''

## 함수 정의부 ===================================================

def bfs(s): ## bfs 는 너비 우선 탐색.
    queue = [] # queue 배열 생성
    queue.append(s) # 큐에 시작노드 삽입

    ans_bfs.append(s) # s를 방문한 노드에 넣는다.
    arr[s] = 1 # s번쨰 값을 방문햇음을 표기하기 위해 1로 값을 바꾼다.
    ## 여기까지는 dfs와 동일하다.

    while queue: # queue 배열에 뭔가가 있으면 계속 반복.
            c = queue.pop(0) # queue에서 하나씩 꺼낸다.
            # print(c)
            # print(queue)
            for n in adj[c]:
                if not arr[n]: # 1이 아니면 
                    queue.append(n)
                    ans_bfs.append(n)
                    arr[n] = 1

## 입력부 ========================================================

n, m, v = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m):
    head_edge, tail_edge = map(int, input().split())
    adj[head_edge].append(tail_edge)
    adj[tail_edge].append(head_edge)

for n in range(1, n+1):
    adj[n].sort()

arr = [0] * (n+1)
ans_bfs = []


## 출력부 ========================================================

bfs(v)

print(*ans_bfs)


