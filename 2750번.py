'''
수 정렬하기

n개의 수가 주어졌을 때, 오름차순 정렬 프로그램 작성
'''

n = int(input())

a = [0] * n
for i in range(n):
    a[i] = int(input())

'''
# min = a[0]
#print(min)
for i in range(n):
    min = a[i] # 2 3 5 5
    for j in range(i+1, n):
        if min > a[j]:
            #min = a[j] # min은 2로 바꼈다. 3 4
            a[i] = a[j] 
            # 2 5 3 4 1 
            # 1 5 3 4 2
            # 1 3 5 4 2
            # 1 2 5 4 3
            # 1 2 4 5 3
            # 1 2 3 5 4
            # 1 2 3 4 5 
            # 2 3 4 1 5
            # 2 1 4 3 5
            # 2 1 3 4 5
'''

a.sort()

for i in range(n):
    print(a[i])