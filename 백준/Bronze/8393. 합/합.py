n = int(input())
score = 0

for i in range(n):
    i += 1
    score += i
    if i == n:
        break

print(score)