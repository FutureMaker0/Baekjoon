'''
두 수의 합

여러 개의 서로다른 정수 집합 S와 또 다른 정수 K가 주어졌을 떄,
S에 속하는 서로 다른 두 개의 정수으 ㅣ합이 K에 가장 가까운 두 정수를
구하시오.
예를 들어, 10개의 정수 S = {-7,9,2,-4,12,1,5,-3,-2,0}이 주어지면
K=8에 그 합이 가장 가까운 두 정수는 12,-4이다.

이게 근삿값이 아닌 만들어질 수 있는지 여부를 찾는 문제가 되면
굉장히 낮은 티어가 될 것이다.

1. 입력을 받는다
2. 이분탐색을 고민한다.
3. 이분탐색은 정렬된 리스트를 기준으로 하므로 리스트 정렬
4. k가 목푯값. - 두 수의 합을 통해 만들어야 되는 값.
    --> 여기서는 동일한값 또는 최근사값의 갯수
5. 리스트를 정렬해서 start+end 했을 때 목푶값 k보다 작으면
    start를 우측으로 한칸 민다. k보다 크면 end를 좌측으로 한칸 민다.
6. 그래서 만약 목표값과 같아지면 걔는 하나의 쌍을 찾은 것이므로
    cnt를 하나 높여준다.
7. 



'''

cnt = 0
def binary_search(arr, target, start, end):
    global cnt
    if arr[start] + arr[end] == target:
        cnt += 1
    elif arr[start] + arr[end] < target:
        start += 1
        binary_search(arr, target, start, end)
    else:
        end -= 1
        binary_search(arr, target, start, end)
    
    return cnt

T = int(input())
for i in range(T):
    N,K = list(map(int, input().split()))
    S = list(map(int, input().split()))
    S.sort()
    # print(S)

for j in range(T):
    print(binary_search(S, K, 0, N-1))


