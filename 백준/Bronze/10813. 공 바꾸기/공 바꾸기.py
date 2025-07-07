
n, m = map(int, input().split())

baskets = list(range(1, n+1))

#print(*baskets) #리스트 잘 짜졌나 확인

for _ in range(m):
    i, j = map(int, input().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp
    

print(*baskets)