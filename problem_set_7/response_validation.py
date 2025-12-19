import validators

while True:
    email = input("What's your email address?: ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")
