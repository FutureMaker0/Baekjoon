'''
5
1 1 1 6 0
2 7 8 3 1

5 
1 1 0 1 6
0 1 1 1 6
2 7 8 3 1

max 값을 찾아서 앞에서부터 하나씩 매칭시키고, 
걔네둘을 각 리스트에서 제외.

max값 구해서 오름차순 정렬된 data1[i]과 앞에서부터 매칭.
그리고 각 값을 각 배열에서 pop해서 빼주고 다시 반복하는 식.

'''

n = int(input())
data1 = list(map(int, input().split()))
data2 = list(map(int, input().split()))

# data1.sort()
# print(data1, end=' ')
# print(' ')

# data2.sort()
# print(data2)

sum = 0
for i in range(n):
    sum += min(data1) * max(data2)
    data1.pop(data1.index(min(data1)))
    data2.pop(data2.index(max(data2)))

print(sum)

'''
max = data2[0]
excep_value = 0
for i in range(n):
    if max < data2[i]:
        max = data2[i]
    # print(max)

    excep_value = max * data1[0]    
print(excep_value)
'''

'''
rank_data2 = []
max = data2[0]
for i in range(n):
    if max <= data2[i]:
        max = data2[i]
print(max)
'''

'''
arr = [[0] * n for _ in range(n)]

total = 0
for i in range(n):
    arr[i] = data1[i] * data2[i*(-1)]
    total += arr[i]
    print(total)
print(total)
'''
