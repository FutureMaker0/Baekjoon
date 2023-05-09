'''

'''

N = int(input())
arr = list(map,(int, input().split()))

ans = [-1] * N
stack = [0]

for i in range(1, N):
    # 만약 스택의 마지막 인덱스의 arr값이 해당 비교하고자 하는 값보다
    # 작으면 그 값보다 클 때까지 해당 값을 오른쪽 수로 설정
    while stack and arr[stack[-1]] < arr[i]:
        


