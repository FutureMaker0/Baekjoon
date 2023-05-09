'''
세탁소 사장 동혁

거스름돈 문제
'''

coin_types = [25, 10, 5, 1]
t = int(input())

result = []
count = 0

for i in range(t):
    a = int(input())

    for j in range(len(coin_types)):
        count = a // coin_types[j]
        result.append(count)
        a %= coin_types[j]

print(*result) # *결과값을 출력하면 배열이 아니라 일반 정숫값으로 출력된다. ★★★

'''
for second in second_types:
        count = t // second
        result.append(count) # append 함수를 잘 활용하자.
        t = t % second
    # print(t)

    # print(result[0], result[1], result[2], end=' ')
    for i in range(len(second_types)):
        print(result[i], end=' ')
'''