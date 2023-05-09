'''
바이너리 써치 이진탐색은 정렬된 데이터를 반으로 나누어 탐색하는
방법이다.

이진탐색의 핵심:
정렬, 파라미터(비교당할 배열, 비교할 배열(타겟), start, end)

'''

import sys

n = int(input())
# n1 = list(map(int, input().split()))
card = list(map(int, sys.stdin.readline().split()))

m = int(input())
# m1 = list(map(int, input().split()))
check = list(map(int, sys.stdin.readline().split()))

card.sort()
# print(card)
# result = [0] * m

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binary_search(card, check[i], 0, n-1) is None:
        print(0, end=' ')
    else:
        print(1, end=' ')





