from store import Store
from exceptions import InvalidPriceError, ProductNotFoundError

def show_menu():
    print("\nInventory Manager")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. List Product")
    print("4. Exit")

def main():
    store = Store("data.csv")
    while True:
        show_menu()
        choice = input("👉 Choose: ").strip()

        try:
            if choice == '1':
                name = input("Product Name: ").capitalize()
                while True:
                    try:
                        price = float(input("Input Price: "))
                        if price < 0:
                            raise InvalidPriceError
                        break
                    except InvalidPriceError:
                        print("❌ Negative Price, Re-enter.")
                    except ValueError:
                        print("❌ Not a Number, Re-enter.")
                store.add_product(name, price)
                print("✅ Product Added Successfully")

            elif choice == '2':
                name = input("Product Name: ")
                store.remove_product(name)
                print("✅ Product Remove Successfully")

            elif choice == '3':
                products = store.list_product()
                if not products:
                    print("Dont Have Any Products")
                for p in products:
                    print(f"{p.name} - ${p.price}")

            elif choice == '4':
                print("Bye")
                break
            else:
                print("❌ Invalid Choice")

        except ValueError:
            print("❌ Price must be a number")
        except InvalidPriceError as e:
            print(e)
        except ProductNotFoundError as e:
            print(e)

if __name__ == "__main__":
    main()