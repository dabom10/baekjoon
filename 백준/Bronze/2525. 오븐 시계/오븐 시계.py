hour, minute = map(int, input().split())
time = int(input())

minute += time
hour += (minute // 60) 

if minute >= 60:
    minute -= 60 * (minute // 60)
    if hour % 24 >= 0:
        hour = 0 + (hour % 24)

print(hour, minute)