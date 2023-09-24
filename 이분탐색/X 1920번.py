'''
n개의 정수가 주어졌을 때, 이 안에 x라는 정수가 존재하는지 알아내는
프로그램 작성

'''

import sys
sys.stdin = open("C:\jocoding\백준\이분(진) 탐색\input\BS 1920번.txt")

n = int(input())
# n1 = list(map(int, input().split()))
card = list(map(int, sys.stdin.readline().split()))

m = int(input())
# m1 = list(map(int, input().split()))
check = list(map(int, sys.stdin.readline().split()))

card.sort()

def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None    

for i in range(m):
    if(bs(card, check[i], 0, n-1)) == None:
        print(0)
    else:
        print(1)

