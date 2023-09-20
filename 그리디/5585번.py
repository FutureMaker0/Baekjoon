a = int(input())
rest = 1000 - a

# print(a,rest)

coin_types = [500, 100, 50, 10, 5, 1]

count = 0
for coin in coin_types:
    count = count + rest//coin
    rest = rest % coin

print(count)
