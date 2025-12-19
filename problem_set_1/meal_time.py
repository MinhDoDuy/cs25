#5 Meal Time
def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60
time = input("What time is it ?: ")
t = convert(time)

if 7 <= t <= 10:
    print("Its breakfast time")
elif 11 <= t <= 13:
    print("Its lunch time")
elif 17 <= t <= 20:
    print("Its dinner time")
else:
    print("Its snack time")
