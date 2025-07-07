num = list(map(int, [input() for _ in range(9)]))

for i in range(9):
    if num[i] == max(num):
        order = i+1

print(max(num), '\n'+ str(order))
