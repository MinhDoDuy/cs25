# students = [
#     {"name": "Hermione", "house": "Gyffindor"},
#     {"name": "Harry", "house": "Gyffindor"},
#     {"name": "Ron", "house": "Gyffindor"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Padma", "house": "Ravenclaw"},
# ]
#
# houses = set()
# for student in students:
#     houses.add(student["house"])
# for house in sorted(houses):
#     print(house)

# class Account:
#     def __init__(self, balance = 0):
#         self._balance = balance
#
#     @property
#     def balance(self):
#         return self._balance
#
#     def deposit(self, n):
#         self._balance += n
#
#     def withdraw(self, n):
#         self._balance -= n
#
# def main():
#     account = Account()
#     print("Balance:", account.balance)
#     account.deposit(100)
#     account.withdraw(50)
#     print("Balance:", account.balance)
#
# if __name__ == "__main__":
#     main()

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")