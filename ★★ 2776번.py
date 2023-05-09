'''
암기왕

연종이는 하루동안 본 정수들을 모두 기억할 수 있다.

연종이 실제 본 정수: 수첩1
연종이 봣다고 하는 순자: 수첩2

수첩2에 적혀있는 순서대로 각 수에 대하여, 수첩1에 있으면 1을
없으면 0을 출력하는 프로그램 작성

## 수첩2에 적혀있는 M개의 숫자 순서대로, 수첩1에 있으면 숫자 1을,
없으면 0을 출력한다.

딱보면 for문 돌려서 오지게 돌리면 되긴 하겠지만 시간초과 날 거다.

'''
'''
T = int(input())
for _ in range(T):
    N = int(input())
    s1 = list(map(int, input().split()))
    # s1.sort()
    M = int(input())
    s2 = list(map(int, input().split()))


for i in s2:       # 1 3 7 9 5
    if i in s1:    # 이게 된다고??????????????
        print(1)
    else:
        print(0)
'''

## s1 = 1 2 3 4 5
## s2 = 1 3 7 9 5

def binary_search(s, e, s2_i, s1):
    while s <= e:
        mid = (s + e) // 2  # mid = 2

        if s1[mid] == s2_i:
            return 1
        elif s1[mid] > s2_i:
            e = mid - 1
        else:
            s = mid + 1
    return 0
            
T = int(input())
for _ in range(T):
    N = int(input())
    s1 = list(map(int, input().split()))
    s1.sort()
    M = int(input())
    s2 = list(map(int, input().split()))

    for i in s2:
        print(binary_search(0, N-1, i, s1))



## https://alpyrithm.tistory.com/139
