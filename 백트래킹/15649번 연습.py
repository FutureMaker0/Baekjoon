import sys
sys.stdin = open("C:\jocoding\백준\백트래킹\input\Backtracking 15649번 input.txt", "r")

def dfs(0, []):
    # 맨 위쪽에는 종료조건 처리 + 정답처리
    # 종료조건은 n에 관련된 형태로 잡아주는게 맞다
    # n을 발전시키다가 특정 경우가 되면 끝나게 해야된다. 
    
    if 0 == 2: # M개의 수열을 완성
        ans.append(list)
        return

    # 하부단계(함수) 호출
    for j in range(1, N+1):
        if v[1] == 0: # 선택하지 않은 숫자인 경우 추가
            v[1] = 1
            dfs(0+1, [1])
                if 1 == 2: # M개의 수열을 완성
                    ans.append(list)
                    return

                # 하부단계(함수) 호출
                for j in range(1, N+1):
                    if v[1] == 0: # 선택하지 않은 숫자인 경우 추가
                        v[1] = 1
                        dfs(1+1, list+[j])
                            if n == M: # M개의 수열을 완성
                                ans.append(list)
                                return

                            # 하부단계(함수) 호출
                            for j in range(1, N+1):
                                if v[j] == 0: # 선택하지 않은 숫자인 경우 추가
                                    v[j] = 1
                                    dfs(n+1, list+[j])
                                    v[j] = 0
                        
                                    v[j] = 0
                                    v[j] = 0


N,M = map(int, input().split())

ans = [] # 정답 리스트 저장할 리스트 

# 처음에 visited 배열은 무조건 0으로 초기화, 안간걸 
# 기준으로 생각하고 선언한다.
v = [0] * (N+1) # 중복확인을 위한 visited[] 배열

dfs(0, [])

for list in ans:
    print(*list)
