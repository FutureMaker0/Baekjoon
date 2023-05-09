'''
1. 반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복 while q:
2. 모든 트럭을 확인하고 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게의 합이
   다리의 하중보다 작을 때 트럭을 다리에 추가하고, 아니면 빈 공간 추가
3. 1,2를 반복하면 모든 트럭이 다 지나가고 다리의 칸이 0이 되어 반복문 종료
4. 이 때의 카운트 출력

'''

import sys

n, w, l = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
bridge = [0] * w # 다리의 칸
cnt = 0

# 반복문을 통해 다리의 모든 트럭이 지나갈 때까지 반복
while bridge:
    cnt += 1 # 카운트
    bridge.pop(0) # 다리의 칸을 하나씩 줄인다.

    # 모든 트럭을 확인
    if a:
        # 현재 다리에 있는 트럭과 다리를 건너려는 트럭의 무게가
        # 다리의 하중보다 크다면 빈 공간을 추가
        if sum(bridge) + a[0] > l:
            bridge.append(0)

        # 다리의 하중보다 작다면 트럭을 다리에 추가
        else:
            bridge.append(a.pop(0))

print(cnt)