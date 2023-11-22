n = int(input())

stack = []
for _ in range(n):
    stack.append(int(input()))

# print(stack)

last_bong = stack[-1]
# print(last_bong)

cnt = 1
for i in reversed(range(n)):
    # print(i)
    if stack[i] > last_bong:
        cnt += 1
        # last_bong = stack[i]

print(cnt)
