'''
대표값2

값 5개 입력받아서

평균값
중앙값
구하기

https://bio-info.tistory.com/157

### 정수 1개 입력받기
N = int(input())
 
### 한줄 정수 리스트 입력받기
li = [*map(int,input().split())]
 
### 여러개 정수 입력받기
a,b,c = map(int,input().split())
 
### 여러 줄의 정수 리스트 입력받기
n = int(input())
li = [int(input()) for _ in range(n)]
## n 없이 한 줄로
li = [int(input()) for _ in range(int(input()))]
 
### N행 배열 입력받기
#### 숫자인 경우
N=int(input()) # N개의 행
arr=[[*map(int,input().split())] for _ in range(N)]
 
#### 문자열인 경우
N=int(input()) # N개의 행
arr=[list(input()) for _ in range(N)]
 
## 입력 빠르게하기
import sys
input=sys.stdin.readline # input함수 바꾸기


'''
# n = [int(input()) for _ in range(int(input()))]

# for _ in range(int(input())):
#    n = int(input())

arr = []
sum = 0
for i in range(5):
    arr.append(int(input()))
    sum += arr[i]

# print(arr)

arr.sort()

print("%d" %(sum / 5))
print(arr[5//2])

