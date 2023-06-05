'''
자연수 N,M이 주어졌을 때, 조건을 만족하는 길이 M인 수열 구하기

-. 1부터 N까지 자연수 중 중복 없이 M개를 고른 수열
-. 고른 수열은 오름차순

함수는 내가 만드는 내 세상이다.
필요에 따라 필요한 파라미터를 적절히 넘겨주어서 활용할 수 있어야 한다.

브루트-포스 알고리즘 = 완전 탐색 알고리즘
즉, 발생할 수 있는 모든 경우를 무식하게 탐색한다는 의미

'''

# import sys
# sys.stdin = open("C:\jocoding\백준\백트래킹\input\Backtracking 15650 input.txt", "r")

N,M = map(int, input().split())

def dfs(n, s, list):

    if n == M:
        result.append(list)
        return

    for j in range(s, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, j+1, list + [j])
            v[j] = 0

    '''
    for j in range(1, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, list + [j])
            v[j] = 0
    '''

result = []
v = [0] * (N+1)

dfs(0, 1, []) # 멀티트리 형태

# 출력가지고 장난치면 안된다.
# 함수 정의 내에서 알고리즘을 수정해야 된다.
for ans in result:
    print(*ans)


