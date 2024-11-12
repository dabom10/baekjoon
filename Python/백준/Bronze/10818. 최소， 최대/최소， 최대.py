n = int(input())
num = list(map(int, input().split()))
max = num[0]
min = num[0]

for i in range(0, n, 1):
    if num[i] > max:
        max = num[i]
    if  min > num[i]:
        min = num[i]

print(f"{min} {max}")
