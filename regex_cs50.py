import re

email = input("What your email: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# import re
#
# name = input("What your name: ").strip()
# if matches := re.search(r"^(.+), *(.+)$", name):
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")

# import re


url = input("URL: ").strip()
matches = re.search(r"^https?://(?:www\.)?twitter\.(?:com|org)/([a-z0-9_]+)", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(1))
