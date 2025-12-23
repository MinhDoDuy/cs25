import re

email = input("What's your email address?: ").strip()

if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.(edu|com|net)$", email):
    print("Valid")
else:
    print("Invalid")
