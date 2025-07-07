total = int(input())

amount = int(input())

total_cheak = 0

for i in range(amount):
    price, num = map(int, input().split())
    total_cheak += price * num

if total == total_cheak:
    print('Yes')
else:
    print('No')