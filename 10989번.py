'''
n개의 수가 주어졌을 때, 오름차순 정렬 프로그램 작성
'''

## 메모리 초과 코드
## sort 함수를 쓰면 보통 메모리 초과에서 자유롭지 못하다
'''
N = int(input())

arr = []
for i in range(N):
    a = int(input())
    arr.append(a)

arr.sort()

for i in range(N):
    print(arr[i])
'''

## 계수정렬을 이용해보자.
## 중복되는 게 있을 때는 계수정렬??
## 저장된 배열의 갯수만큼 돌면서 배열 값이 아닌 해당 인덱스를
## 출력하는 것이다 ★★

## pypy3에서는 런타임에러, python3에서는 정답으로 인정...

import sys

N = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(N):
    data = int(sys.stdin.readline())
    arr[data] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)

'''
5
data: 1 1 5 2 2

arr[1] = 2 - 2번 반복
arr[5] = 1 - 1번 반복
arr[2] = 2 - 2번 반복

1 1 2 2 5
'''

