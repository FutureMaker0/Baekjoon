'''
permutation 함수를 사용한 dfs 백트래킹 문제 풀이

'''

from itertools import permutations

N,M = map(int, input().split())

arr = [i for i in range(1, N+1)]

p = list(permutations(arr, M))

for result in p:
    print(*result)

