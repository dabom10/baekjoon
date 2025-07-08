import sys

n, m = map(int, input().split())
baskets = []

for i in range(n):
    i += 1
    baskets.append(i) # 바구니에 1부터 n까지 번호 넣기 == baskets = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(*baskets)