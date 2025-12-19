#1 Fuel Gauge
while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0 or x > y:
            continue

        percent = round(x / y * 100)

        if percent <= 1:
            print("E")
        if percent >= 99:
            print("F")
        else:
            print(f"Remaining: {percent}% Fuel")
        break
    except (ValueError, ZeroDivisionError):
        pass