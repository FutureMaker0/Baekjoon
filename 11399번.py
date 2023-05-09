'''
ATM 앞에 N명이 줄을 서있다.
1~N번까지 있으며, i번 사람이 인출하는데 걸리는 시간은 pi이다.

p1=3, p2=1, p3=4, p4=3, p5=2 라고 하고

1,2,3,4,5 순서대로 줄을 선다고 가정하자.

1번 사람은 3분만에 돈 인출가능.
2번 사람은 4분
3번 사람은 8분
4번 사람은 11분
5번 사람은 13분 걸린다.
이 경우 모든 사람이 돈을 다 뽑는데 필요한 시간은 다 더한 값인
39분이다.

2,5,1,4,3 순서로 줄을 서면
2번 사람은 1분
5번 사람은 3분
1번 사람은 6분
4번 사람은 9분
3번 사람은 13분
총 시간은 32분이 걸린다.

시간의 합의 최솟값을 구하는 프로그램 작성하라.

'''

'''
p1 = 3
p2 = 1
p3 = 4
p4 = 3
p5 = 2
'''

n = int(input())
data = list(map(int, input().split()))

# print(data)
'''
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
print(array)
'''

data.sort()
# print(data)

arr = []
total = 0

# 이건 입력받기 위한 배열
for i in range(n):
    arr.append(0)

for i in range(n):
    '''
    arr[0] = data[0] 
    arr[1] = data[0] + data[1]
    arr[2] = data[0] + data[1] + data[2]
    arr[3] = data[0] + data[1] + data[2] + data[3]
    arr[4] = data[0] + data[1] + data[2] + data[3] + data[4]
    '''
    # arr[i] += data[i]
    arr[i] = arr[i-1] + data[i]
    
    total += arr[i]

print(total)

'''
1
1+2
1+2+3
1+2+3+3
1+2+3+3+4
'''
