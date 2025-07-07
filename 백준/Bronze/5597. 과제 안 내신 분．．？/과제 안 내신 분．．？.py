student = list(range(1, 31))

submitted = []

for i in range(28):
    submitted.append(int(input()))

missing = [s for s in student if s not in submitted]

missing.sort()

print(missing[0])
print(missing[1])