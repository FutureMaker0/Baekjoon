t = int(input())

second_types = [300, 60, 10]
result = []
count = 0

if t%10 != 0:
    print(-1)

else:
    for second in second_types:
        count = t // second
        result.append(count)
        t = t % second
    # print(t)

    # print(result[0], result[1], result[2], end=' ')
    for i in range(len(second_types)):
        print(result[i], end=' ')
