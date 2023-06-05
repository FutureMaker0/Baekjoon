'''
팰린드롬인지 판별하는 불린 출력, recursion 함수 호출횟수


'''

def recursion(s, l, r):
    if l >= r:
        return 1, (l+1)
    elif s[l] != s[r]: 
        return 0, (l+1)
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
arr = [[] for _ in range(T)]
# count = [[0] for _ in range(T)] 

for i in range(T):
    arr[i] = input()
    # str = arr[i]
    # print(len(str))
    # print(arr[i])
    
for i in range(T):
    print(*isPalindrome(arr[i])) #, recursion 횟수)
    # print(*count[i])





# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))





