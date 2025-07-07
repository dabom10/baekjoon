import sys

n, m = map(int, input().split())

baskets = [0] * n

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i-1, j):
        baskets[x] = k

print(*baskets)