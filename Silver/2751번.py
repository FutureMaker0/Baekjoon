'''
수 정렬하기2

'''

n = int(input())

arr = [0] * (n)
for i in range(n):
    arr[i] = int(input())

arr.sort()
for i in range(n):
    print(arr[i])

