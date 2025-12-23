import re

email = input("What's yours email address: ").strip()
if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9]+\.(com|edu|net)$", email):
    print("Valid Email")
else:
    print("Invalid Email")