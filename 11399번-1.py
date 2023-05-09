'''
총 5명이 있고, 
P1 = 3 
P2 = 1 
P3 = 4 
P4 = 3 
P5 = 2

3 1 4 3 2 = 3 + 4 + 8 + 11 + 13 = 39
1 2 3 3 4 = 1 + 3 + 6 + 9 + 13 = 32

'''
n = int(input())

'''
for i in range(n):
    a = map(int, input().split())
    print(a[i])
'''

a = list(map(int, input().split()))
# print(a)

a.sort()
# print(a)

time = 0
total = 0
# total = [0,0,0,0,0]
for i in range(n):
    time += a[i]
    total += time
    # print(time, end=' ')
print(total)

'''
a[0]
a[0] + a[1]
a[0] + a[1] + a[2]
a[0] + a[1] + a[2] + a[3]
a[0] + a[1] + a[2] + a[3] + a[4]
'''