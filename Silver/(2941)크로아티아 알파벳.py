N = str(input())

li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

answer = 0
for i in li:
    N = N.replace(i, '*')

print(len(N))
