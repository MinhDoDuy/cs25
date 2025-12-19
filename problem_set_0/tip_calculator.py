#5 Tip Calculator
bill = float(input("Enter bill: "))
tip_percent = float(input("Enter tip: "))

tip = bill * tip_percent / 100
total = bill + tip
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")