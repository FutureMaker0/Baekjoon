'''
좌표 정렬하기 2

2차원 평면 위의 점 N개가 주어진다. 
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 
정렬한 다음 출력하는 프로그램을 작성하시오.

y를 우선순위로 오름차순 정렬하되, y가 같으면
x를 기준으로 오름차순 정렬

'''

n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr.sort(key = lambda x : (x[1], x[0]))
    # 여기서의 x는 그냥 람다함수 안에서 사용하기 위한 지역변수
    # x[1] 인자 기준으로 우선 정렬한 후,
    # 그 안에서 x[0] 기준으로 재정렬.
    # --> 조건부 정렬 같은 느낌.

for i in arr:
    # print(arr[i])
    print(i[0], i[1])

