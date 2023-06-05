'''
전자레인지 버튼 시간의 합 맞추기.

5분 = 300초
1분 = 60초
10초 = 10초

3개 버튼으로 시간을 맞출 수 없는 경우 -1을 출력

'''

t = int(input())

second_types = [300, 60, 10]
result = []
count = 0

if t%10 != 0:
    print(-1)

else:
    for second in second_types:
        count = t // second
        result.append(count) # append 함수를 잘 활용하자.
        t = t % second
    # print(t)

    # print(result[0], result[1], result[2], end=' ')
    for i in range(len(second_types)):
        print(result[i], end=' ')


'''
a = int(input())
rest = 1000 - a

# print(a,rest)

coin_types = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coin_types:
    count = count + rest//coin
    rest = rest % coin

print(count)
'''
