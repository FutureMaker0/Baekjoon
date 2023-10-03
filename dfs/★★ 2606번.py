'''
신종 바이러스인 웜 바이러스는 네트웤을 통해 전파된다. 
하나가 걸리면 연결된 애들은 다걸린다.

서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 
웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램 작성

뎁스 우선이기 때문에 하나 노드를 정하면 아래 달려있느 것들을
일괄로 다 탐색하고 다음으로 넘어간다.

dfs는 adj 이중행렬을 쓴다.

갯수만 알면 되기 때문에 dfs가 훨씬 간단할 수 있다.

dfs로 현재 current가 몇번 감염됐느냐

dfs(1) 번부터 시작.

v = [0] * (n+1)개를 만들어야 될 꺼다. 
0번 인덱스를 안쓰기 때문에.

ans = 0

감염된 pc 수가 늘었다: ans += 1
v[c] = 1 # visited 배열에 현재 노드가 감염됐다고 1로 표기 
해야될 단위 작업

첫 번째 문제에서는 낮은 순서대로 가라고 해서 오름차순 정렬
했지만 지금 문제는 갯수만 세면 되므로 정렬 필요없이 그냥 진행

이전에 있었떤 것 처럼,
눈에 보이게 연결 배열이나, 비지티드 배열
변수들을 만들어놓고 손으로 설계하면서 정리를 하면 좋다.

'''

# import sys
# sys.stdin = open("C:\jocoding\백준\DFS\input\dfs 2606 input.txt", "r")

def dfs(c):
    global ans

    ans += 1
    v[c] = 1

    for n in adj[c]: # current 노드와 연결된 모든 노드 처리 
        if not v[n]:
            dfs(n)

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())

    adj[s].append(e)
    adj[e].append(s)

ans = 0
v = [0] * (N+1)

dfs(1)

print(ans-1)

