'''
우유축제

딸기우유 > 초코우유 > 바나나우유 > 딸기우유

0: 딸기우유
1: 초코우유
2: 바나나우유

0 1 2 0 1 2 0
딸 초 바 딸 초 바 딸

주어진 제한횟수 속에서 0 1 2 순서쌍이 몇 번 반복되는가?

s[0] = 0, count%3 = 0 --> count+1 = 1
s[1] = 1, count%3 = 1 --> count+1 = 2
s[2] = 2, count%3 = 2 --> count+1 = 3
s[3] = 0, count%3 = 0 --> count+1 = 4


0 2 2 2 2 2 인 경우,
s[0] = 0, count%3 = 0 --> count+1 = 1
s[1] = 2, count%3 = 1 --> count 유지
s[2] = 2, count%3 = 1 --> count 유지

뭔가 점화식이 생각이 안 날 떈, % mod 연산을 적극 떠올려보자.

'''

n = int(input())
s = list(map(int, input().split()))

count = 0
for i in range(n):
    if s[i] == count % 3:
        count += 1

print(count)


