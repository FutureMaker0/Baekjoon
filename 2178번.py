'''
n*m 크기의 배열로 표현되는 미로가 있다.

미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸
(1,1) 에서 출발하여 (n,m)의 위치로 이동할 때 지나야 하는
최소의 칸 수를 구하는 프로그램 작성.
서로 인접한 칸으로만 이동할 수 있다. 

이게 어떻게 bfs 알고리즘이 적용이 되는걸까?...

맵에도 적는 방법이 있지만, 문제가 복잡해지면 맵하고
visited를 별도 운영하는게 좋은 경우가 많다.
가장 효율적이고 짧은 코드보다는 실수를 줄일 수 있고
실수했을 떄 눈에 잘 보이는 형태로 짜는걸 목표로 한다.

bfs는 애매하면 visited를 디버거랑 같이 써보면서 하는 것도
의미가 있다.

bfs의 기본 틀은...

'''

'''
bfs(si, sj, ei, ej)

1. queue 생성
2. queue 초기데이터 삽입, visited[si][sj] = 1로 초기화
3. while q:
    ci, cj = q.pop() # 하나꺼내준다
    4방향, 조건에 맞으면(배열 범위 내, arr == 1, visited == 0)
    조건에 맞으면 q에 삽입.
    visited[ni][nj] = v[ci][cj] + 1

큰 틀에서 bfs를 많이 풀어봤따면 전형적인 문제가 된다.

굉장히 기본적인 문제다!

SWEA?

'''

# import sys
# sys.stdin = open("C:\jocoding\백준\BFS\BFS 2178 input.txt", "r")

N, M = map(int,(input().split()))
arr = [list(map(int, input())) for _ in range(N)]

def bfs(si, sj, ei, ej):
    q = [] # QUEUE
    v = [[0] * M for _ in range(N)] # VISITED 배열

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0) # 커런트에 큐에서 하나 빼온 값 넣음
        
        # 정답처리가 필요한 경우 이 자리에서...
        if (ci, cj) == (ei, ej):
            return v[ei][ej] 


        # 범위내, 4방향, 조건에 맞으면 큐에 삽입
        # 조건이란: arr == 1, v == 0
        # delta
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci + di, cj + dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1


ans = bfs(0, 0, N-1, M-1)
print(ans)


