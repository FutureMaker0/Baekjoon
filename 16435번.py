'''
스네이크버드
새대가리를 단 뱀

과일 하나를 먹으면 길이가 1만큼 늘어난다.

과일은 지상으로부터 일정높이 떨어져 있으며 i개 있다.

스네이크버드는 지보다 작거나 같은 높이의 과일만 먹는다.

과일을 먹어 늘릴 수 있는 최대 길이 구하라.

입력값: 과일의 갯수, 초기 스네이크버드 몸길이
        과일의 높이

출력값: 스네이크버드의 최대길이 출력

'''

n, l = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

for i in range(n):
    if h[i] > l:
        continue
    else:
        h[i] <= l
        l += 1

print(l)






