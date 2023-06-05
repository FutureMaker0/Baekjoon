'''
별찍기

input 입력 받아서, 해당 수까지 별의 갯수를 늘려가면서 출력
'''

n = int(input())

for i in range(1, n+1):
    print('*' * i)
