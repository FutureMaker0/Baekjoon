'''
나무 자르기

# 예제 입력
4 7
20 15 10 17

--> 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는
    최댓값 출력
정렬된 값: 10 15 17 20
    

# 예제 출력
15

'''
'''
import sys
sys.setrecursionlimit(10**7)

result = 0
def binary_search(N, arr, temp_target, target): 
    global result
    for i in range(N):
        # print(arr[i], end=' ')

        if arr[i] < temp_target:
            continue
        else:
            result += (arr[i] - temp_target)
        # print(result)

    if result > target:
        # temp_target += 1
        binary_search(N, a, t+1, M)
    else:
        return temp_target

N, M = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()

total = 0
for j in range(N):
    total += a[j]
    t = total // N
print(t)

ans = binary_search(N, a, t, M)
# print(ans)
'''

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

start, end = 1, a[N-1]

while start <= end:
    mid = (start + end) // 2

    result = 0
    for comp in a:
        if comp < mid:
            continue
        else:
            result += (comp - mid) 

    ## 여기 밑에 네줄이 핵심이다!! start, end값 조정해가며 결과값 도출
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)







