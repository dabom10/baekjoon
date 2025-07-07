n = int(input())

a = list(map(int, input().split()))

v = int(input())
cheak = 0

for i in range(n):
    if a[i] == v:
        cheak += 1

print(cheak)