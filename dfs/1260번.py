'''
dfs와 bfs 비교
'''

'''
# 함수 정의
def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    arr[c] = 1          # 방문 표시

    for n in adj[c]:
        if not arr[n]: # next 노드가 아직 방문하지 않았다면,
            dfs(n)

def bfs(s):
    q = [] # 필요한 q, v[], 변수  생성
    
    q.append(s) # 큐에 시작 데이터 삽입
    ans_bfs.append(s)
    arr[s] = 1

    while q:
        c = q.pop(0)
        # c에서 연결되어 있는 애들을 하나씩 꺼낸다
        for n in adj[c]:
            # 안가본 노드면 큐에 삽입하면 된다.
            if not arr[n]:
                q.append(n)
                ans_bfs.append(n)
                arr[n] = 1


n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향

for i in range(1, n+1):
    adj[i].sort() # 오름차순으로 정렬

# 함수는 제일 마지막에 짜는 거다.

arr = [0] * (n+1)
ans_dfs = []
dfs(v)

arr = [0] * (n+1)
ans_bfs = []
bfs(v)

print(*ans_dfs)
print(*ans_bfs)
'''

'''
필요한 변수들을 실명으로 범위 조심해서 만들어놓고
오름차순같은 조건들은 미리 정리해놓고,

bfs는 큐에다 넣어놓고 순차적으로 방문하도록 만드는 것이다.


'''


## 함수 정의부 ============================================

## dfs 는 깊이 우선 탐색...
def dfs(c): # 출발 노드를 현재 current node로 받는다.
    ans_dfs.append(c) # c를 방문한 노드에 넣는다.
    arr[c] = 1 # c가 방문된 노드임을 표기하기 위해 1로 값을 준다.
    # 여기까지가 사전 전처리 작업 느낌.

    for n in adj[c]:
        if not arr[n]: # arr[n]의 값이 1이 아니라면,
            dfs(n)         

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

## 입력부 =================================================

n, m, v = map(int, input().split())

adj = [[] for _ in range(n+1)]

for _ in range(m): # 간선의 갯수만큼
    head_edge, tail_edge = map(int, input().split())
    adj[head_edge].append(tail_edge)
    adj[tail_edge].append(head_edge)

for i in range(1, n+1):
    adj[i].sort() 


# 아래 두 개의 배열이 뭘 위한 배열인지 의미하는게 중요하다.
arr = [0] * (n+1) # 방문한 노드의 값을 1로 표현하기 위한 배열
ans_dfs = [] # 방문된 노드들을 담기 위한 배열, 그냥 순서 상관없이 가는 순서대로 담는다.
dfs(v) # 시작노드를 dfs 함수에 대입.

arr = [0] * (n+1)
ans_bfs = []
bfs(v) # 시작노드를 bfs 함수에 대입.

## 출력부 =================================================

# print(ans_dfs) # 배열 형식으로 출력
print(*ans_dfs) # 정수 리스트 형식으로 출력

# print(ans_bfs) # 배열 형식으로 출력
print(*ans_bfs) # 정수 리스트 형식으로 출력

