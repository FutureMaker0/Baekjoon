'''
큐 연산과정 보여주는 프로그램 작성

## 파일 입출력 과정에서 인풋파일 읽어들이면 런타임 초과 뜬다.
'''

import sys
from collections import deque

# sys.stdin = open("C:\jocoding\백준\스택, 큐\큐\input18258.txt", "r")

N = int(sys.stdin.readline())
q = deque([])

for _ in range(N):
    s = sys.stdin.readline().split()

    if s[0] == "push":
        q.append(s[1])
    
    elif s[0] == "pop":
        if not q:
            print(-1)
        else:
            print(q.popleft())
    
    elif s[0] == "size":
        print(len(q))
    
    elif s[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    
    elif s[0] == "front":
        if not q:
            print(-1)
        else:
            print(q[0])
    
    elif s[0] == "back":
        if not q:
            print(-1)
        else:
            print(q[-1])


