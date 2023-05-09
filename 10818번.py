'''
세 정수 a,b,c가 주어질 떄 두 번쨰로 큰 정수 출력
'''

A,B,C = list(map(int, input().split()))

arr = [A,B,C]
arr.sort()

print(arr[1])
