from cookie_jar import Jar

def main():
    capacity = int(input("Enter jar capacity (Tổng số bánh quy): "))
    jar = Jar(capacity)

    while True:
        print("\nCurrent jar:", jar)
        print("1. Deposit cookies")
        print("2. Withdraw cookies")
        print("3. All Cookies")
        print("4. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                n = int(input("How many cookies to deposit? "))
                jar.deposit(n)
            elif choice == "2":
                n = int(input("How many cookies to withdraw? "))
                jar.withdraw(n)
            elif choice == '3':
                print(f"All cookie: {jar} -", jar.size())
            elif choice == "4":
                print("Bye!")
                break
            else:
                print("Invalid choice")
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
