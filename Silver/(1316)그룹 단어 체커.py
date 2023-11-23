T = int(input())

answer = T
for i in range(T):
    N = str(input())

    '''
    문자열 그룹단어 여부 판별 알고리즘
    - 연속성이 끊겼을 때 다시 해당 문자가 안나오면 cnt+1
    '''

    for j in range(len(N)-1):
        if N[j] == N[j+1]:
            pass
        elif N[j] in N[j+1:]:
            answer -= 1
            break

print(answer)
