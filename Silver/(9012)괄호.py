T = int(input())

for _ in range(T):
    N = str(input())
    # print(N)

    stack = []
    for elem in N:
        if elem == '(':
            stack.append(elem)
            # print(stack)

        elif elem == ')':
            if not stack:
                print('NO')
                break
            else:
                stack.pop()

    # # print(' ')
    else:
        print(stack)
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')

