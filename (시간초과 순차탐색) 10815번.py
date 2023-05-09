'''
숫자카드

상근이가 n장의 카드를 가지고 있다.
m장의 카드가 주어지는데 그 중 상근이가 갖고 잇는 카드면
1을 출력, 없는 카드면 0을 출력해라.

list(map()) 으로 정수를 받으면 list 자체가 하나의 배열이 된다.
인덱스 활용해서 원하는 값을 뺄 수 있다.

바이너리 서치 문제다.
그렇게 한번 해보자.

처음에 했던 아래 방식대로 하면 순차탐색이기 때문에 시간초과가
백퍼 나온다.

'''

import sys

n = int(input())
# n1 = list(map(int, input().split()))
n1 = list(map(int, sys.stdin.readline().split()))


m = int(input())
# m1 = list(map(int, input().split()))
m1 = list(map(int, sys.stdin.readline().split()))

# print(m1)
# print(m1[1])

result = [0] * m


# 일치하는걸 찾아서 1로 바꿨다가 그 다음에
# 불일치하는게 나오면 다시 0으로 바뀌어버린다.
for i in range(m):
    # print(m1[i])
    for j in range(n):
        # print(n1[j])
        if m1[i] == n1[j]:
            result[i] = 1
            continue
             
print(*result)


