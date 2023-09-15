'''
백설공주와 일곱 난쟁이

키의 합이 100이 되는 케이스를 찾아 오름차순으로 출력하라
키의 합이 100이 되는 케이스를 찾아 오름차순으로 출력하라
'''

# import sys
# from collections import deque

arr = [0] * 9
for i in range(9):
    arr[i] = int(input())
    # q = deque(int(input()))

# print(arr)
arr.sort()
sum = sum(arr)
# sorted(q)
# print(q)

## 총 합계에서 100에서 초과하는 값 만큼의 합을 가지는
## 두 개의 수를 제외하고 출력해주면 된다.

total = 0
target = sum - 100
'''
for h in arr:
    total += h
    while total < target:
        if sum == target:
            print(h)
        else:
'''

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        


