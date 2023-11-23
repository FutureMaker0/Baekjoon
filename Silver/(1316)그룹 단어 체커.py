T = int(input())

answer = T
for i in range(T):
    N = str(input())

    for j in range(len(N)-1):
        if N[j] == N[j+1]:
            pass
        elif N[j] in N[j+1:]:
            answer -= 1
            break

print(answer)
