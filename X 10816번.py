'''
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 n개를 가지고 있다. 정수 m개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는
프로그램 작성


'''

import sys
sys.stdin = open("C:\jocoding\백준\이분(진) 탐색\input\BS 10816번.txt")

n = int(input())
# n1 = list(map(int, input().split()))
card = list(map(int, sys.stdin.readline().split()))

m = int(input())
# m1 = list(map(int, input().split()))
check = list(map(int, sys.stdin.readline().split()))

card.sort()
print(card)
# result = [0] * m

# -10 -10 2 3 3 6 7 10 10 10

global count
# count = 0
count = 0
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        global count
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            count += 1
            start = mid
            return count
    return None

for i in range(m):
    if(binary_search(card, check[i], 0, n-1)) is None:
        print(0, end=' ')
    else:
        print(count, end=' ')










