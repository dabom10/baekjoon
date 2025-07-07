import sys

n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    n = i + 1
    print(f"Case #{n}:",a+b)