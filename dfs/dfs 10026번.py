'''
적록색약

이코테 5-8.py 예제 참고

dfs 알고리즘은 재귀함수 호출을 통해 해결한다.

,,, too hard

★★★ 깊이 우선 탐색 - 골드티어
https://konghana01.tistory.com/72


접근 방법
1. 적록색약이 아닌 사람의 경우에는 R,G,B를 차례로 DFS 탐색
2. 우선 R을 제일 먼저 탐색한다고 가정하면, N*N의 그림을 하나하나
   모두 탐색하며 만약 해당 위치를 아직 방문하지 않았고, 해당 위치의
   값이 R이라면 DFS를 동작시킨다. 
3. 알파벳별로 DFS가 모두 끝날 때마다 하나씩 숫자를 카운트한다.
4. G와 B도 2,3번을 똑같이 반복하며 탐색한다.
5. 적록색약인 사람의 경우에는 G를 R로 바꾼 뒤(R을 G로 바꿔도 무방),
   2,3번을 반복한다.

'''

## ======================================================================= 입력부
import sys, copy
from collections import deque
sys.setrecursionlimit(10**6) 
# 재귀 깊이가 최대 100x100 = 10000이 될 수 있기에 재귀 깊이를 늘려준다.

n = int(sys.stdin.readline()) # input()대신 sys.stdin.readline()으로 하자.
painting = [sys.stdin.readline().rstrip() for _ in range(n)]
direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

## ===================================================================함수 정의부
def dfs(row, col, target):
    """ 
    row : 그림의 row
    col : 그림의 col
    target : 탐색하고자하는 색깔 ('R', 'G', 'B')
    """
    visited[col][row] = True # 현재 위치 방문 처리
    for drow, dcol in direction: # 상하좌우에 대한 방향 받기
        new_row = row+drow
        new_col = col+dcol
        # 현재위치의 상하좌우에 해당하는 위치가 주어진 범위 이내인지, 아직 방문하지 않았는지, 탐색하고자 하는 색깔인지 파악 후 모두 맞을 경우, DFS탐색
        if 0<=new_row<=n-1 and 0<=new_col<=n-1 and not visited[new_col][new_row] and painting_[new_col][new_row] == target:
            dfs(new_row, new_col, target)

    # dfs 함수 정의 자체는 길지않다.
    # 미리 설정해놓은 좌표값을 가지고 for문을 돌리며,
    # 입력한 영역을 벗어나지 않는 조건을 달고 그 안에 해당한다면,
    # dfs 알고리즘 재귀적 수행

## 출력부 ======================================================================
# 적록색약이 아닌 경우, 적록 색약인 경우로 나누어 실행
# for문을 활용해서 2번을 돌린다. false, true인 경우로 나누어서.
for red_green_blindness in [False, True]: 
    
    painting_ = copy.deepcopy(painting) 
    # 적록색약의 경우 painting의 값을 바꿔야하기에 이를 deepcopy한다.
    visited = [[False for _ in range(n)] for _ in range(n)] 
    # 방문 처리를 위한 리스트
    
    count = 0 # 구역의 수 초기화
    if red_green_blindness:
        for i in range(n):
            painting_[i] = painting[i].replace('G', 'R')  
            # 적록색약의 경우 G -> R로 값 변경
            # false일 경우에는 수행하지 않는 조건문.
            # 두번쨰 true일때만 실행되어서 g, r을 서로 바꾸어주는 코드.

    # R, G, B에 대해 한번씩 탐색한다.
    # 적록색약 일때, 아닐때 2번 동작. 
    # 적록색약일 경우에는 g가 r로 치환되었기 때문에 r,b에 대해서만 탐색한다.
    for target in ['R', 'G', 'B']:
        for col in range(n):
            for row in range(n):
                if not visited[col][row] and painting_[col][row] == target: 
                    # 아직 방문하지 않은 위치이고, 탐색하고자하는 색깔일 때 DFS 탐색 
                    # 시작
                    dfs(row, col, target)
                    count += 1 # 한 구역에 대한 DFS 탐색이 완료되면 카운트 증가
    print(count)



