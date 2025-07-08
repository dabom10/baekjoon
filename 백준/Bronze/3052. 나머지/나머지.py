num = []

for _ in range(10):
    a = int(input())
    b = a % 42
    num.append(b)

value = len(set(num))

print(value)
