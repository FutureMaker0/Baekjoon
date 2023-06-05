'''
소트인사이드

배열을 정렬하는 것은 쉽다. 
수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
'''

n = int(input())

#print(len(str(n)))

#result = sorted(str(n), reverse=True)
arr= []
for i in str(n):
    arr.append(int(i)) # append 함수 적극 활용
    # arr = list(map(int, str(n)))

arr.sort(reverse=True)

for i in arr:
    print(i, end='')

