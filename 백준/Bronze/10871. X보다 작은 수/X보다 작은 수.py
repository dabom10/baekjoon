amount, cutnum = map(int, input().split())
num = list(map(int, input().split()))

for i in range(amount):
    if num[i] < cutnum:
       print(num[i], end=' ')