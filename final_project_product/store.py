import csv
from exceptions import InvalidPriceError, ProductNotFoundError

class Product:
    def __init__(self, name, price):
        if price < 0:
            raise InvalidPriceError("❌ Price must be greater than 0")
        self.name = name
        self.price = price

class Store:
    def __init__(self, filename):
        self.filename = filename
        self.products = self.load_products()

    def load_products(self):
        products = []
        try:
            with open(self.filename, newline="", encoding="utf-8") as file:
                #with dùng để đảm bảo k hông bị leak tài dữ liệu ra ngoài
                #encoding="" dùng để k bắt lỗi tiếng việt
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(
                        Product(row["name"], float(row["price"]))
                    )
        except FileNotFoundError:
            pass
        return products

    def save_products(self):
        with open(self.filename, "w", newline="", encoding="utf-8") as file:
            #Mở file ở chế độ write
            #Mỗi lần ghi là ghi đè cả file
            #Đảm bảo dữ liệu đồng bộ
            writer = csv.DictWriter(file, fieldnames=["name", "price"]) #csv sẽ có 2 cột
            writer.writeheader() #ghi dòng tiêu đề name,price
            for p in self.products:
                writer.writerow({
                    "name": p.name,
                    "price": p.price
                })

    def add_product(self, name, price):
        self.products.append(Product(name, price))
        self.save_products()

    def remove_product(self, name):
        for p in self.products:
            if p.name == name:
                self.products.remove(p)
                self.save_products()
                return
        raise ProductNotFoundError("❌ Product not found")

    def list_product(self):
        return self.products