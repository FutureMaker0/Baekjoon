'''
별찍기

input 입력 받아서, 해당 수까지 별의 갯수를 늘려가면서 출력

5번째 자리에 별 출력
4,5번쨰 자리에 별출력

5 들어오면, n-1만큼 ' ' 출력 후  * 출력
           n-2만큼 ' ' 출력 후 * 출력
           n-3만큼 ' ' 출력 후 * 출력
           n-4만큼 ' ' 출력 후 * 출력
           n-5만큼 ' ' 출력 후 * 출력

'''

n = int(input())

for i in range(n, 0, -1):
    print(' ' * (n-i) + '*' * i)


## 두 개를 연달아 출력할 때,
## , 를 사용하게 되면 공백이 하나 붙고 다음꺼가 출력
## + 를 사용하게 되면 공백 없이 바로 이어 붙여서 출력!! 
